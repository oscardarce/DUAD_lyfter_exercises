-- Ejercio Lyfter BD Shop Practice
CREATE TABLE Department (
    Department_ID VARCHAR(25) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);
CREATE TABLE Products (
    Product_ID VARCHAR(25) PRIMARY KEY,
    Name VARCHAR(150) NOT NULL,
    Code VARCHAR(25) NOT NULL UNIQUE,
    Price DECIMAL(12, 2) NOT NULL,
    Stock INT NOT NULL DEFAULT 0,
    Description VARCHAR(255),
    Department_ID VARCHAR(25) NOT NULL,
    FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
);
CREATE TABLE Users (
    User_ID VARCHAR(25) PRIMARY KEY,
    Name VARCHAR(150) NOT NULL,
    Phone VARCHAR(25),
    Email VARCHAR(150) NOT NULL UNIQUE,
    Address VARCHAR(255),
    Registration_Date DATE NOT NULL,
    Status VARCHAR(10) NOT NULL DEFAULT 'Activo'
);
CREATE TABLE Invoices (
    Invoice_ID VARCHAR(25) PRIMARY KEY,
    User_ID VARCHAR(25) NOT NULL,
    Date DATE NOT NULL,
    Final_Total DECIMAL(12, 2) NOT NULL DEFAULT 0,
    Payment_Type VARCHAR(25) NOT NULL,
    Status VARCHAR(25) NOT NULL DEFAULT 'Activa',
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);
CREATE TABLE Invoice_Detail (
    Detail_ID VARCHAR(25) PRIMARY KEY,
    Invoice_ID VARCHAR(25) NOT NULL,
    Product_ID VARCHAR(25) NOT NULL,
    Quantity INT NOT NULL,
    Unit_Price DECIMAL(12, 2) NOT NULL,
    Subtotal DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (Invoice_ID) REFERENCES Invoices(Invoice_ID),
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);
-- Data
INSERT INTO Department
VALUES ('DEPT-1', 'Electronica'),
    ('DEPT-2', 'Ropa'),
    ('DEPT-3', 'Hogar'),
    ('DEPT-4', 'Abarrotes');
INSERT INTO Products
VALUES (
        'PROD-1',
        'Laptop Asus',
        'LAP-1',
        450000,
        15,
        'Laptop 15 pulgadas 16GB RAM',
        'DEPT-1'
    ),
    (
        'PROD-2',
        'Camisa Red Point',
        'CAM-2',
        25000,
        80,
        'Camisa de algodon talla M',
        'DEPT-2'
    ),
    (
        'PROD-3',
        'Sarten Members Selection',
        'SAR-3',
        18500,
        40,
        'Sarten 28cm antiadherente',
        'DEPT-3'
    ),
    (
        'PROD-4',
        'Arroz Tio Pelon 5kg',
        'ARR-4',
        3200,
        200,
        'Arroz blanco grano largo',
        'DEPT-4'
    );
INSERT INTO Users
VALUES (
        'USR-1',
        'Maria Perez',
        '8888-1234',
        'maria@gmail.com',
        'San Jose, CR',
        '2024-01-10',
        'Activo'
    ),
    (
        'USR-2',
        'Carlos Mora',
        '7777-5678',
        'carlos@gmail.com',
        'Heredia, CR',
        '2024-03-22',
        'Activo'
    ),
    (
        'USR-3',
        'Ana Jimenez',
        '6666-9012',
        'ana@gmail.com',
        'Cartago, CR',
        '2023-11-05',
        'Inactivo'
    );
INSERT INTO Invoices
VALUES (
        'FAC-1',
        'USR-1',
        '2024-04-01',
        475000,
        'Tarjeta',
        'Activa'
    ),
    (
        'FAC-2',
        'USR-2',
        '2024-04-03',
        28200,
        'Efectivo',
        'Activa'
    ),
    (
        'FAC-3',
        'USR-1',
        '2024-04-09',
        21700,
        'SINPE',
        'Activa'
    );
INSERT INTO Invoice_Detail
VALUES ('DET-1', 'FAC-1', 'PROD-1', 1, 450000, 450000),
    ('DET-2', 'FAC-1', 'PROD-2', 1, 25000, 25000),
    ('DET-3', 'FAC-2', 'PROD-2', 1, 25000, 25000),
    ('DET-4', 'FAC-2', 'PROD-4', 1, 3200, 3200),
    ('DET-5', 'FAC-3', 'PROD-3', 1, 18500, 18500),
    ('DET-6', 'FAC-3', 'PROD-4', 1, 3200, 3200);
-- Transacción de compra
DO $$
DECLARE v_user_exists INT;
v_available_stock INT;
v_unit_price DECIMAL(12, 2);
v_subtotal DECIMAL(12, 2);
v_grand_total DECIMAL(12, 2) := 0;
v_detail_id VARCHAR(25);
v_product_id VARCHAR(25);
v_quantity INT;
i INT;
p_Invoice_ID VARCHAR(25) := 'FAC-10';
p_User_ID VARCHAR(25) := 'USR-2';
p_Payment_Type VARCHAR(20) := 'SINPE';
-- Cada fila representa: (ID_Detalle, ID_Producto, Cantidad)
p_Items TEXT [] [] := ARRAY [
        ARRAY['DET-20', 'PROD-2', '2'],
ARRAY ['DET-21', 'PROD-4', '3'] ];
BEGIN -- Verificar que el usuario existe y esta activo
SELECT COUNT(*) INTO v_user_exists
FROM Users
WHERE User_ID = p_User_ID
    AND Status = 'Activo';
IF v_user_exists = 0 THEN RAISE EXCEPTION 'El usuario % no existe o no esta activo.',
p_User_ID;
END IF;
-- Insertar la factura con total en 0, se actualiza al final
INSERT INTO Invoices (
        Invoice_ID,
        User_ID,
        Date,
        Final_Total,
        Payment_Type,
        Status
    )
VALUES (
        p_Invoice_ID,
        p_User_ID,
        CURRENT_DATE,
        0,
        p_Payment_Type,
        'Activa'
    );
-- Recorrer cada producto en la lista
FOR i IN 1..array_length(p_Items, 1) LOOP v_detail_id := p_Items [i] [1];
v_product_id := p_Items [i] [2];
v_quantity := p_Items [i] [3]::INT;
-- Verificar que el producto existe y tiene stock suficiente
SELECT Stock,
    Price INTO v_available_stock,
    v_unit_price
FROM Products
WHERE Product_ID = v_product_id;
IF v_available_stock IS NULL THEN RAISE EXCEPTION 'El producto % no existe.',
v_product_id;
END IF;
IF v_available_stock < v_quantity THEN RAISE EXCEPTION 'Stock insuficiente para %. Disponible: %. Solicitado: %.',
v_product_id,
v_available_stock,
v_quantity;
END IF;
-- Calcular el subtotal de este producto
v_subtotal := v_unit_price * v_quantity;
v_grand_total := v_grand_total + v_subtotal;
-- Insertar el detalle de este producto
INSERT INTO Invoice_Detail (
        Detail_ID,
        Invoice_ID,
        Product_ID,
        Quantity,
        Unit_Price,
        Subtotal
    )
VALUES (
        v_detail_id,
        p_Invoice_ID,
        v_product_id,
        v_quantity,
        v_unit_price,
        v_subtotal
    );
-- Reducir el stock del producto
UPDATE Products
SET Stock = Stock - v_quantity
WHERE Product_ID = v_product_id;
END LOOP;
-- Actualizar el total final de la factura con la suma de todos los productos
UPDATE Invoices
SET Final_Total = v_grand_total
WHERE Invoice_ID = p_Invoice_ID;
RAISE NOTICE 'Compra registrada. Factura: %. Total: %.',
p_Invoice_ID,
v_grand_total;
EXCEPTION
WHEN OTHERS THEN RAISE EXCEPTION 'Error en la compra: %. Transaccion cancelada.',
SQLERRM;
END $$;
--  Transacción de retorno
DO $$
DECLARE v_invoice_status VARCHAR(25);
v_detail RECORD;
p_Invoice_ID VARCHAR(10) := 'FAC-10';
BEGIN -- Verificar que la factura existe y esta activa
SELECT Status INTO v_invoice_status
FROM Invoices
WHERE Invoice_ID = p_Invoice_ID;
IF v_invoice_status IS NULL THEN RAISE EXCEPTION 'La factura % no existe.',
p_Invoice_ID;
END IF;
IF v_invoice_status != 'Activa' THEN RAISE EXCEPTION 'La factura % no puede retornarse. Estado actual: %.',
p_Invoice_ID,
v_invoice_status;
END IF;
-- Recorrer todos los productos de la factura y restaurar el stock de cada uno
FOR v_detail IN
SELECT Product_ID,
    Quantity
FROM Invoice_Detail
WHERE Invoice_ID = p_Invoice_ID LOOP
UPDATE Products
SET Stock = Stock + v_detail.Quantity
WHERE Product_ID = v_detail.Product_ID;
END LOOP;
-- Marcar la factura como Retornada
UPDATE Invoices
SET Status = 'Retornada'
WHERE Invoice_ID = p_Invoice_ID;
RAISE NOTICE 'Retorno procesado. Factura: % marcada como Retornada.',
p_Invoice_ID;
EXCEPTION
WHEN OTHERS THEN RAISE EXCEPTION 'Error en el retorno: %. Transaccion cancelada.',
SQLERRM;
END $$;