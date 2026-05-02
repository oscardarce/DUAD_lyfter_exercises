-- Ya el auto increimento solo aplica con INTEGER no con INT y  no hace falta declararlo solo esto ya se autogenera comportamiento especial del ROWID
-- Tabla Usuario
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    email VARCHAR(25) NOT NULL,
    register_date TIMESTAMP NOT NULL
);
---- Tabla Producto
CREATE TABLE product (
    id INTEGER PRIMARY KEY,
    code INT NOT NULL,
    name VARCHAR(25) NOT NULL,
    price DECIMAL NOT NULL,
    entry_date TIMESTAMP NOT NULL,
    brand VARCHAR(25) NOT NULL
);
---- Tabla Facturas
CREATE TABLE bill(
    id INTEGER PRIMARY KEY,
    id_user INT REFERENCES user(id),
    bill_number INT NOT NULL,
    purchase_date TIMESTAMP NOT NULL,
    total_amount DECIMAL NOT NULL
);
---- Tabla Metodos de pago
CREATE TABLE payment_method (
    id INTEGER PRIMARY KEY,
    method_type VARCHAR(25) NOT NULL,
    bank_name VARCHAR(25) NOT NULL
);
---- Tabla Carrito de compras
CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY,
    id_user INT REFERENCES user(id),
    id_product INT REFERENCES product(id),
    cart_state VARCHAR(25) NOT NULL
);
-- Tabla Cruz Metodo de pago de la factura
CREATE TABLE bill_payment_method(
    id INTEGER PRIMARY KEY,
    id_bill INT REFERENCES bill(id),
    id_payment_method INT REFERENCES payment_method(id)
);
---- Tabla Cruz Producto Carrito
CREATE TABLE product_shopping_cart(
    id INTEGER PRIMARY KEY,
    id_product INT REFERENCES product(id),
    id_shopping_cart INT REFERENCES shopping_cart(id)
);
---- Tabla Cruz Factura Compra (detalle)
CREATE TABLE product_bill_detail(
    id INTEGER PRIMARY KEY,
    id_product INT REFERENCES product(id),
    id_bill INT REFERENCES bill(id),
    purchased_amount INT NOT NULL,
    total_amount INT NOT NULL
);
--Tabla Cruz Productos por Usuario (E-commerce)
CREATE TABLE user_product(
    id INTEGER PRIMARY KEY,
    id_user INT REFERENCES user(id),
    id_product INT REFERENCES product(id)
);
--Tabla Cruz Reseña de producto
CREATE TABLE product_review(
    id INTEGER PRIMARY KEY,
    id_product INT REFERENCES product(id),
    id_user INT REFERENCES user(id),
    review VARCHAR(255) NOT NULL,
    product_rating SMALLINT NOT NULL,
    date_review TIMESTAMP NOT NULL
);
--Creación de columnas de número de telefono del comprador y código del empleado que realiza la venta
--Se debe crear la tabla con default en '' porque ya fue creada con anterioridad en caso de existir registros estos tendran pro defecto una cadena de texto vacia
ALTER TABLE bill
ADD buyer_phone_number VARCHAR(25) NOT NULL DEFAULT '';
ALTER TABLE bill
ADD employee_code INT NOT NULL DEFAULT 0;
----Insersión de datos para hacer SELETCS de pruena
INSERT INTO user (id, name, email, register_date)
VALUES (
        1,
        'Oscar Darce',
        'oscardarce@gmail.com',
        '2026-02-10 10:00:00'
    ),
    (
        2,
        'Maria Lopez',
        'maria@gmail.com',
        '2026-02-11 11:30:00'
    ),
    (
        3,
        'Roberto Carlos',
        'carlos@gmail.com',
        '2026-02-12 09:15:00'
    );
INSERT INTO product (id, code, name, price, entry_date, brand)
VALUES (
        1,
        1001,
        'Laptop DELL',
        500000.00,
        '2026-02-01 08:00:00',
        'Lenovo'
    ),
    (
        2,
        1002,
        'Mouse Incott',
        25000.00,
        '2026-02-02 09:00:00',
        'Logitech'
    ),
    (
        3,
        1003,
        'Teclado EPOMAKER',
        45000.00,
        '2026-02-03 10:00:00',
        'Redragon'
    );
INSERT INTO bill (
        id,
        id_user,
        bill_number,
        purchase_date,
        total_amount,
        buyer_phone_number,
        employee_code
    )
VALUES (
        1,
        1,
        5001,
        '2026-02-12 12:00:00',
        775.50,
        '85871047',
        101
    ),
    (
        2,
        2,
        5002,
        '2026-02-12 13:30:00',
        45.99,
        '88887777',
        102
    );
INSERT INTO payment_method (id, method_type, bank_name)
VALUES (1, 'Tarjeta Crédito', 'BAC'),
    (2, 'SINPE', 'BN'),
    (3, 'Efectivo', 'N/A');
INSERT INTO product_bill_detail (
        id,
        id_product,
        id_bill,
        purchased_amount,
        total_amount
    )
VALUES (1, 1, 1, 1, 500000),
    (2, 2, 1, 1, 25000),
    (3, 3, 2, 1, 45000);
INSERT INTO shopping_cart (id, id_user, id_product, cart_state)
VALUES (1, 1, 2, 'Activo'),
    (2, 2, 3, 'Comprado');
--1.Obtenga todos los productos almacenados
SELECT *
FROM product;
--2. Obtenga todos los productos que tengan un precio mayor a 50000
SELECT *
FROM product
WHERE price > 5000;
--3.Obtenga todas las compras de un mismo producto por id.
SELECT *
FROM product_bill_detail
WHERE id_product = 1;
--4.Obtenga todas las compras agrupadas por producto,
--donde se muestre el total comprado entre todas las compras.
SELECT id_product,
    SUM(purchased_amount) AS total_purchased
FROM product_bill_detail
GROUP BY id_product;
--5.Obtenga todas las facturas realizadas por el mismo comprador
SELECT *
FROM bill
WHERE id_user = 1;
--6.Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT *
FROM bill
ORDER BY total_amount DESC;
--7.Obtenga una sola factura por número de factura.
SELECT *
FROM bill
WHERE bill_number = 5001;