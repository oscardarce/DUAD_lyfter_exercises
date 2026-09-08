from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from functools import wraps
from pathlib import Path

from flask import Flask, g, jsonify, request
from werkzeug.exceptions import HTTPException

from db import (
    ClientNotFoundError,
    DB_Manager,
    DuplicateUsernameError,
    InsufficientStockError,
    ProductInUseError,
    ProductNotFoundError,
)
from jwt_manager import JWT_Manager


app = Flask("sales-service")

BASE_DIRECTORY = Path(__file__).resolve().parent

_db_manager = None
_jwt_manager = None


def get_db_manager():
    global _db_manager
    if _db_manager is None:
        _db_manager = DB_Manager()
    return _db_manager


def get_jwt_manager():
    global _jwt_manager
    if _jwt_manager is None:
        _jwt_manager = JWT_Manager(
            BASE_DIRECTORY / "keys" / "private_key.pem",
            BASE_DIRECTORY / "keys" / "public_key.pem",
        )
    return _jwt_manager


class APIError(Exception):
    def __init__(self, message, status=400, **details):
        self.message = message
        self.status = status
        self.details = details


def api_error(message, status, **details):
    return jsonify(error=message, **details), status


@app.errorhandler(APIError)
def handle_api_error(error):
    return api_error(error.message, error.status, **error.details)


@app.errorhandler(DuplicateUsernameError)
def handle_duplicate_username(_error):
    return api_error("El nombre de usuario ya existe", 409)


@app.errorhandler(ClientNotFoundError)
def handle_missing_client(_error):
    return api_error("Cliente no encontrado", 404)


@app.errorhandler(ProductNotFoundError)
def handle_missing_product(error):
    return api_error(
        "Producto no encontrado",
        404,
        product_id=error.product_id,
    )


@app.errorhandler(InsufficientStockError)
def handle_insufficient_stock(error):
    return api_error(
        "Inventario insuficiente",
        409,
        product_id=error.product_id,
        requested=error.requested,
        available=error.available,
    )


@app.errorhandler(ProductInUseError)
def handle_product_in_use(_error):
    return api_error(
        "El producto no puede eliminarse porque aparece en una factura",
        409,
    )


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    if isinstance(error, HTTPException):
        return error
    app.logger.exception("Error inesperado", exc_info=error)
    return api_error("Ocurrió un error interno", 500)


# --- Autenticación / autorización ---
def require_auth(*allowed_types):
    # Sin argumentos (@require_auth()) solo exige un token válido. Con argumentos además exige que account_type esté en esa lista

    def decorator(view):
        @wraps(view)
        def wrapper(*args, **kwargs):
            authorization = request.headers.get("Authorization", "")
            if not authorization.startswith("Bearer "):
                raise APIError("Se requiere un token de autenticación", 401)

            token = authorization.removeprefix("Bearer ").strip()
            decoded = get_jwt_manager().decode(token) if token else None
            if not decoded:
                raise APIError("El token es inválido", 401)

            account_type = decoded.get("account_type")
            account_id = decoded.get("id")
            if account_type not in {"admin", "client"} or account_id is None:
                raise APIError("El token es inválido", 401)
            if allowed_types and account_type not in allowed_types:
                raise APIError("No tiene permisos para esta operación", 403)
            # g es el objeto "por request" de Flask cualquier vista puede leer g.identity después sin tener que volver a decodificar el token.
            g.identity = {"id": account_id, "account_type": account_type}
            return view(*args, **kwargs)

        return wrapper

    return decorator


# --- Validación de entrada ---
def required_json(*fields):
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        raise APIError("Debe enviar un objeto JSON")

    missing = [field for field in fields if data.get(field) is None]
    if missing:
        raise APIError("Faltan campos requeridos", fields=missing)
    return data


def parse_integer(value, field, minimum=0):
    try:
        parsed = int(str(value))
        if parsed < minimum:
            raise ValueError
        return parsed
    except (TypeError, ValueError):
        raise APIError(
            f"{field} debe ser un entero mayor o igual a {minimum}"
        ) from None


def parse_decimal(value, field):
    # Decimal(str(value)) evita error de precisión binaria
    try:
        parsed = Decimal(str(value))
        if not parsed.is_finite() or parsed < 0:
            raise InvalidOperation
        return parsed
    except (InvalidOperation, TypeError, ValueError):
        raise APIError(
            f"{field} debe ser un número mayor o igual a cero"
        ) from None


def validate_credentials():
    data = required_json("username", "password")
    username = data["username"]
    password = data["password"]

    if not isinstance(username, str) or not username.strip():
        raise APIError("Username es requerido")
    if len(username.strip()) > 30:
        raise APIError("Username no puede superar 30 caracteres")
    if not isinstance(password, str) or not password:
        raise APIError("Password es requerido")
    return username.strip(), password


def validate_product():
    data = required_json("name", "price", "quantity", "date_of_entry")
    name = data["name"]

    if not isinstance(name, str) or not name.strip():
        raise APIError("El nombre no puede estar vacío")
    if len(name.strip()) > 30:
        raise APIError("El nombre no puede superar 30 caracteres")

    try:
        entry_date = datetime.strptime(
            data["date_of_entry"],
            "%Y-%m-%d",
        ).date()
    except (TypeError, ValueError):
        raise APIError(
            "date_of_entry debe tener el formato YYYY-MM-DD"
        ) from None

    return {
        "name": name.strip(),
        "price": parse_decimal(data["price"], "price"),
        "quantity": parse_integer(data["quantity"], "quantity"),
        "date_of_entry": entry_date,
    }


def validate_sale_products(products):
    if not isinstance(products, list) or not products:
        raise APIError("Debe enviar al menos un producto")

    # Si el cliente manda el mismo product_id repetido en dos líneas distintas del body, se agrupan sumando cantidades en vez de crear dos InvoiceItem separados para el mismo producto.
    grouped = {}
    for position, product in enumerate(products):
        if not isinstance(product, dict):
            raise APIError("Producto inválido", position=position)
        product_id = parse_integer(product.get("product_id"), "product_id", 1)
        quantity = parse_integer(product.get("quantity"), "quantity", 1)
        grouped[product_id] = grouped.get(product_id, 0) + quantity

    return [
        {"product_id": product_id, "quantity": grouped[product_id]}
        for product_id in sorted(grouped)
    ]


def serialize(value):
    # jsonify/json.dumps no sabe convertir Decimal ni date/datetime convierte esos tipos a string antes de pasarlos a jsonify.
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(item) for item in value]
    return value


# --- Endpoints: autenticación ---
def register_account(account_type, response_key):
    username, password = validate_credentials()
    account = get_db_manager().insert_account(account_type, username, password)
    token = get_jwt_manager().encode(
        {"id": account["id"], "account_type": account_type}
    )
    return jsonify(**{response_key: account}, token=token), 201


def login_account(account_type):
    username, password = validate_credentials()
    account = get_db_manager().get_account(account_type, username, password)
    if not account:
        raise APIError("Credenciales incorrectas", 401)

    token = get_jwt_manager().encode(
        {"id": account["id"], "account_type": account_type}
    )
    return jsonify(token=token), 200


@app.post("/register")
def register_admin():
    return register_account("admin", "administrator")


@app.post("/login")
def login_admin():
    return login_account("admin")


@app.post("/clients/register")
def register_client():
    return register_account("client", "client")


@app.post("/clients/login")
def login_client():
    return login_account("client")


@app.get("/me")
@require_auth("admin", "client")
def me():
    identity = g.identity
    account = get_db_manager().get_account_by_id(
        identity["account_type"],
        identity["id"],
    )
    if not account:
        raise APIError("Cuenta no encontrada", 404)
    return jsonify(**serialize(account), account_type=identity["account_type"])


# --- Endpoints: productos ---
# GET /products y GET /products/<id> admin únicamente.
@app.post("/products")
@require_auth("admin")
def create_product():
    product = get_db_manager().create_product(**validate_product())
    return jsonify(
        message="Producto creado correctamente",
        product=serialize(product),
    ), 201


@app.get("/products")
@require_auth("admin")
def get_products():
    return jsonify(products=serialize(get_db_manager().get_products()))


@app.get("/products/<int:product_id>")
@require_auth("admin")
def get_product_by_id(product_id):
    product = get_db_manager().get_product_by_id(product_id)
    if not product:
        raise APIError("Producto no encontrado", 404)
    return jsonify(product=serialize(product))


@app.put("/products/<int:product_id>")
@require_auth("admin")
def update_product(product_id):
    product = get_db_manager().update_product(product_id, **validate_product())
    if not product:
        raise APIError("Producto no encontrado", 404)
    return jsonify(
        message="Producto actualizado correctamente",
        product=serialize(product),
    )


@app.delete("/products/<int:product_id>")
@require_auth("admin")
def delete_product(product_id):
    deleted_id = get_db_manager().delete_product(product_id)
    if deleted_id is None:
        raise APIError("Producto no encontrado", 404)
    return jsonify(message="Producto eliminado correctamente", id=deleted_id)


# --- Endpoints: ventas / facturas ---
@app.post("/sales")
@require_auth("admin", "client")
def create_sale():
    identity = g.identity
    data = required_json("products")

    if identity["account_type"] == "client":
        client_id = identity["id"]
    else:
        if data.get("client_id") is None:
            raise APIError(
                "client_id es requerido cuando la compra la realiza un administrador"
            )
        client_id = parse_integer(data.get("client_id"), "client_id", 1)

    products = validate_sale_products(data["products"])
    invoice = get_db_manager().create_sale(client_id, products)
    return jsonify(
        message="Venta realizada correctamente",
        invoice=serialize(invoice),
    ), 201


@app.get("/clients/<int:client_id>/invoices")
@require_auth("admin", "client")
def get_client_invoices(client_id):
    identity = g.identity
    # Un cliente puede consultar solo sus propias facturas el admin puede consultar las de cualquiera
    if identity["account_type"] == "client" and identity["id"] != client_id:
        raise APIError("No puede consultar facturas de otro cliente", 403)

    invoices = get_db_manager().get_invoices_by_client_id(client_id)
    if invoices is None:
        raise APIError("Cliente no encontrado", 404)
    return jsonify(client_id=client_id, invoices=serialize(invoices))


@app.get("/invoices/<int:invoice_id>")
@require_auth("admin", "client")
def get_invoice_by_id(invoice_id):
    invoice = get_db_manager().get_invoice_by_id(invoice_id)
    if not invoice:
        raise APIError("Factura no encontrada", 404)
    if (
        g.identity["account_type"] == "client"
        and g.identity["id"] != invoice["client_id"]
    ):
        raise APIError("No puede consultar la factura de otro cliente", 403)
    return jsonify(invoice=serialize(invoice))


if __name__ == "__main__":
    app.run(debug=True)
