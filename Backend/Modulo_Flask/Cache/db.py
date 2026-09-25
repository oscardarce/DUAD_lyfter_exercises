from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload

from db_connection import DbConnection
from models import Administrator, Client, Invoice, InvoiceItem, Product


# Permite reutilizar los mismos métodos (insert_account, get_account, etc.)
# tanto para administradores como para clientes, sin duplicar código:
# account_type ("admin"/"client") decide qué modelo/tabla usar.
ACCOUNT_MODELS = {
    "admin": Administrator,
    "client": Client,
}


# Excepciones propias del dominio. main.py las traduce a códigos HTTP
# específicos (ver los @app.errorhandler en main.py) en vez de que cada
# endpoint tenga que hacer ese chequeo a mano.
class DuplicateUsernameError(Exception):
    pass


class ClientNotFoundError(Exception):
    pass


class ProductInUseError(Exception):
    pass


class ProductNotFoundError(Exception):
    def __init__(self, product_id):
        self.product_id = product_id


class InsufficientStockError(Exception):
    def __init__(self, product_id, requested, available):
        self.product_id = product_id
        self.requested = requested
        self.available = available


class DB_Manager:
    def __init__(self, connection=None):
        self.connection = connection or DbConnection()
        self.connection.setup_database()
        self.Session = self.connection.Session

    # Objeto ORM a dict plano
    @staticmethod
    def _account_dict(account):
        return {
            "id": account.id,
            "username": account.username,
        }

    @staticmethod
    def _product_dict(product):
        return {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "date_of_entry": product.date_of_entry,
            "quantity": product.quantity,
        }

    @staticmethod
    def _invoice_dict(invoice):
        return {
            "id": invoice.id,
            "client_id": invoice.client_id,
            "created_at": invoice.created_at,
            "total": invoice.total,
            "items": [
                {
                    "id": item.id,
                    "invoice_id": item.invoice_id,
                    "product_id": item.product_id,
                    "product_name": item.product_name,
                    "quantity": item.quantity,
                    "unit_price": item.unit_price,
                    "subtotal": item.subtotal,
                }
                for item in invoice.items
            ],
        }

    # --- Cuentas (admin / cliente) ---
    def insert_account(self, account_type, username, password):
        model = ACCOUNT_MODELS[account_type]
        account = model(username=username, password=password)

        try:
            # Session.begin(): abre transacción, hace commit automático al salir del bloque sin errores, y rollback automático si hay excepción
            with self.Session.begin() as session:
                session.add(account)

            # flush() envía el INSERT a la DB dentro de la transacción (para que account.id quede poblado) sin cerrarla todavía  el commit ocurre al salir del "with".
                session.flush()
            return self._account_dict(account)
        except IntegrityError as error:
            # Salta cuando username ya existe
            raise DuplicateUsernameError from error

    def get_account(self, account_type, username, password):
        model = ACCOUNT_MODELS[account_type]
        stmt = select(model).where(
            model.username == username,
            model.password == password,
        )

        with self.Session() as session:
            account = session.scalar(stmt)
            return self._account_dict(account) if account else None

    def get_account_by_id(self, account_type, account_id):
        model = ACCOUNT_MODELS[account_type]

        with self.Session() as session:
            account = session.get(model, account_id)
            return self._account_dict(account) if account else None

    # --- Productos ---
    def create_product(self, **values):
        product = Product(**values)

        with self.Session.begin() as session:
            session.add(product)
            session.flush()
        return self._product_dict(product)

    def get_products(self):
        stmt = select(Product).order_by(Product.id)

        with self.Session() as session:
            products = session.scalars(stmt).all()
            return [self._product_dict(product) for product in products]

    def get_product_by_id(self, product_id):
        with self.Session() as session:
            product = session.get(Product, product_id)
            return self._product_dict(product) if product else None

    def update_product(self, product_id, **values):
        with self.Session.begin() as session:
            product = session.get(Product, product_id)
            if not product:
                return None

            for field, value in values.items():
                setattr(product, field, value)
            session.flush()
        return self._product_dict(product)

    def delete_product(self, product_id):
        try:
            with self.Session.begin() as session:
                product = session.get(Product, product_id)
                if not product:
                    return None

                deleted_id = product.id
                session.delete(product)
            return deleted_id
        except IntegrityError as error:
            # ForeignKey ondelete="RESTRICT" en InvoiceItem.product_id impide  borrar un producto que ya aparece en alguna factura
            raise ProductInUseError from error

    #  Ventas / facturas
    def create_sale(self, client_id, products):
        with self.Session.begin() as session:
            client = session.get(Client, client_id)
            if not client:
                raise ClientNotFoundError

            invoice = Invoice(client=client, total=Decimal("0.00"))
            session.add(invoice)

            # Se ordena por product_id antes de procesar, evita un deadlock donde la transacción A espera el producto que tiene bloqueado B, y B espera el que tiene A.
            for requested in sorted(products, key=lambda item: item["product_id"]):
                product_id = requested["product_id"]
                quantity = requested["quantity"]

                # with_for_update(): bloquea la fila del producto hasta que esta transacción termine. Sin esto, dos compras simultáneas podrían leer el mismo quantity disponible, ambas validar que hay stock, y terminar vendiendo más unidades de las que existen (race condition clásica).
                product = session.scalar(
                    select(Product)
                    .where(Product.id == product_id)
                    .with_for_update()
                )

                if not product:
                    raise ProductNotFoundError(product_id)
                if product.quantity < quantity:
                    raise InsufficientStockError(
                        product_id,
                        quantity,
                        product.quantity,
                    )

                subtotal = product.price * quantity
                invoice.total += subtotal
                invoice.items.append(
                    InvoiceItem(
                        product=product,
                        product_name=product.name,
                        quantity=quantity,
                        unit_price=product.price,
                        subtotal=subtotal,
                    )
                )
                product.quantity -= quantity

            session.flush()
            result = self._invoice_dict(invoice)
        return result

    def get_invoices_by_client_id(self, client_id):
        stmt = (
            select(Invoice)
            # selectinload precarga los items de cada factura en una segunda consulta (en vez de una por factura), evitando el problema N+1 al armar el dict con _invoice_dict.
            .options(selectinload(Invoice.items))
            .where(Invoice.client_id == client_id)
            .order_by(Invoice.created_at.desc(), Invoice.id.desc())
        )

        with self.Session() as session:
            if not session.get(Client, client_id):
                return None

            invoices = session.scalars(stmt).all()
            return [self._invoice_dict(invoice) for invoice in invoices]

    def get_invoice_by_id(self, invoice_id):
        stmt = (
            select(Invoice)
            .options(selectinload(Invoice.items))
            .where(Invoice.id == invoice_id)
        )

        with self.Session() as session:
            invoice = session.scalar(stmt)
            return self._invoice_dict(invoice) if invoice else None
