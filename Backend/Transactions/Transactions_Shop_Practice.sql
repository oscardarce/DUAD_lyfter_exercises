-- Ejercio Lyfter BD Shop Practice

CREATE TABLE Departamentos (
    ID_Departamento VARCHAR(10)  PRIMARY KEY,
    Nombre          VARCHAR(100) NOT NULL
);

CREATE TABLE Productos (
    ID_Producto     VARCHAR(10)    PRIMARY KEY,
    Nombre          VARCHAR(150)   NOT NULL,
    Codigo          VARCHAR(20)    NOT NULL UNIQUE,
    Precio          DECIMAL(12, 2) NOT NULL,
    Stock           INT            NOT NULL DEFAULT 0,
    Descripcion     VARCHAR(255),
    ID_Departamento VARCHAR(25)    NOT NULL,
    FOREIGN KEY (ID_Departamento) REFERENCES Departamentos(ID_Departamento)
);

CREATE TABLE Usuarios (
    ID_Usuario     VARCHAR(25)  PRIMARY KEY,
    Nombre         VARCHAR(150) NOT NULL,
    Telefono       VARCHAR(25),
    Correo         VARCHAR(150) NOT NULL UNIQUE,
    Direccion      VARCHAR(255),
    Fecha_Registro DATE         NOT NULL,
    Estado         VARCHAR(10)  NOT NULL DEFAULT 'Activo'
);

CREATE TABLE Facturas (
    ID_Factura  VARCHAR(25)    PRIMARY KEY,
    ID_Usuario  VARCHAR(25)    NOT NULL,
    Fecha       DATE           NOT NULL,
    Total_Final DECIMAL(12,2)  NOT NULL DEFAULT 0,
    Tipo_Pago   VARCHAR(25)    NOT NULL,
    Estado      VARCHAR(25)    NOT NULL DEFAULT 'Activa',
    FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
);

CREATE TABLE Detalle_Factura (
    ID_Detalle      VARCHAR(25)   PRIMARY KEY,
    ID_Factura      VARCHAR(25)   NOT NULL,
    ID_Producto     VARCHAR(25)   NOT NULL,
    Cantidad        INT           NOT NULL,
    Precio_Unitario DECIMAL(12,2) NOT NULL,
    Subtotal        DECIMAL(12,2) NOT NULL,
    FOREIGN KEY (ID_Factura)  REFERENCES Facturas(ID_Factura),
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto)
);


-- Data

INSERT INTO Departamentos VALUES
    ('DEPT-1', 'Electronica'),
    ('DEPT-2', 'Ropa'),
    ('DEPT-3', 'Hogar'),
    ('DEPT-4', 'Abarrotes');

INSERT INTO Productos VALUES
    ('PROD-1', 'Laptop Asus',         'LAP-1', 450000, 15, 'Laptop 15 pulgadas 16GB RAM',  'DEPT-1'),
    ('PROD-2', 'Camisa Red Point',        'CAM-2',  25000, 80, 'Camisa de algodon talla M',    'DEPT-2'),
    ('PROD-3', 'Sarten Members Selection', 'SAR-3',  18500, 40, 'Sarten 28cm antiadherente',    'DEPT-3'),
    ('PROD-4', 'Arroz Tio Pelon 5kg',            'ARR-4',   3200,200, 'Arroz blanco grano largo',     'DEPT-4');

INSERT INTO Usuarios VALUES
    ('USR-1', 'Maria Perez',  '8888-1234', 'maria@gmail.com',  'San Jose, CR', '2024-01-10', 'Activo'),
    ('USR-2', 'Carlos Mora',  '7777-5678', 'carlos@gmail.com', 'Heredia, CR',  '2024-03-22', 'Activo'),
    ('USR-3', 'Ana Jimenez',  '6666-9012', 'ana@gmail.com',    'Cartago, CR',  '2023-11-05', 'Inactivo');

INSERT INTO Facturas VALUES
    ('FAC-1', 'USR-1', '2024-04-01', 475000, 'Tarjeta', 'Activa'),
    ('FAC-2', 'USR-2', '2024-04-03',  28200, 'Efectivo','Activa'),
    ('FAC-3', 'USR-1', '2024-04-09',  21700, 'SINPE',   'Activa');

INSERT INTO Detalle_Factura VALUES
    ('DET-1', 'FAC-1', 'PROD-1', 1, 450000, 450000),
    ('DET-2', 'FAC-1', 'PROD-2', 1,  25000,  25000),
    ('DET-3', 'FAC-2', 'PROD-2', 1,  25000,  25000),
    ('DET-4', 'FAC-2', 'PROD-4', 1,   3200,   3200),
    ('DET-5', 'FAC-3', 'PROD-3', 1,  18500,  18500),
    ('DET-6', 'FAC-3', 'PROD-4', 1,   3200,   3200);


-- Transacción de compra
DO $$
DECLARE
    v_stock_disponible  INT;
    v_precio_unitario   DECIMAL(12,2);
    v_subtotal          DECIMAL(12,2);
    v_usuario_existe    INT;

    p_ID_Factura  VARCHAR(25)  := 'FAC-10';
    p_ID_Detalle  VARCHAR(25)  := 'DET-20';
    p_ID_Usuario  VARCHAR(25)  := 'USR-2';
    p_ID_Producto VARCHAR(25)  := 'PROD-2';
    p_Cantidad    INT          := 2;
    p_Tipo_Pago   VARCHAR(20)  := 'SINPE';
BEGIN
    -- Verificar que el usuario existe y esta activo
    SELECT COUNT(*) INTO v_usuario_existe
    FROM Usuarios
    WHERE ID_Usuario = p_ID_Usuario
      AND Estado = 'Activo';

    IF v_usuario_existe = 0 THEN
        RAISE EXCEPTION 'El usuario % no existe o no esta activo.', p_ID_Usuario;
    END IF;

    -- Verificar que el producto tiene stock suficiente
    SELECT Stock, Precio INTO v_stock_disponible, v_precio_unitario
    FROM Productos
    WHERE ID_Producto = p_ID_Producto;

    IF v_stock_disponible IS NULL THEN
        RAISE EXCEPTION 'El producto % no existe.', p_ID_Producto;
    END IF;

    IF v_stock_disponible < p_Cantidad THEN
        RAISE EXCEPTION 'Stock insuficiente. Disponible: %. Solicitado: %.', v_stock_disponible, p_Cantidad;
    END IF;

    -- Calcular el subtotal
    v_subtotal := v_precio_unitario * p_Cantidad;

    -- Insertar la factura
    INSERT INTO Facturas (ID_Factura, ID_Usuario, Fecha, Total_Final, Tipo_Pago, Estado)
    VALUES (p_ID_Factura, p_ID_Usuario, CURRENT_DATE, v_subtotal, p_Tipo_Pago, 'Activa');

    -- Insertar el detalle de la factura
    INSERT INTO Detalle_Factura (ID_Detalle, ID_Factura, ID_Producto, Cantidad, Precio_Unitario, Subtotal)
    VALUES (p_ID_Detalle, p_ID_Factura, p_ID_Producto, p_Cantidad, v_precio_unitario, v_subtotal);

    -- Reducir el stock del producto
    UPDATE Productos
    SET Stock = Stock - p_Cantidad
    WHERE ID_Producto = p_ID_Producto;

    RAISE NOTICE 'Compra registrada. Factura: %. Total: %.', p_ID_Factura, v_subtotal;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error en la compra: %. Transaccion cancelada.', SQLERRM;
END $$;


--  Transacción de retorno
DO $$
DECLARE
    v_estado_factura  VARCHAR(25);
    v_ID_Producto     VARCHAR(25);
    v_cantidad_compra INT;

    p_ID_Factura VARCHAR(10) := 'FAC-10';
BEGIN
    -- Verificar que la factura existe y esta activa
    SELECT Estado INTO v_estado_factura
    FROM Facturas
    WHERE ID_Factura = p_ID_Factura;

    IF v_estado_factura IS NULL THEN
        RAISE EXCEPTION 'La factura % no existe.', p_ID_Factura;
    END IF;

    IF v_estado_factura != 'Activa' THEN
        RAISE EXCEPTION 'La factura % no puede retornarse. Estado actual: %.', p_ID_Factura, v_estado_factura;
    END IF;

    -- Obtener el producto y la cantidad registrada en el detalle
    SELECT ID_Producto, Cantidad INTO v_ID_Producto, v_cantidad_compra
    FROM Detalle_Factura
    WHERE ID_Factura = p_ID_Factura
    LIMIT 1;

    -- Restaurar el stock del producto
    UPDATE Productos
    SET Stock = Stock + v_cantidad_compra
    WHERE ID_Producto = v_ID_Producto;

    -- Marcar la factura como Retornada
    UPDATE Facturas
    SET Estado = 'Retornada'
    WHERE ID_Factura = p_ID_Factura;

    RAISE NOTICE 'Retorno procesado. Factura: % marcada como Retornada. Stock restaurado: +% unidades de %.', p_ID_Factura, v_cantidad_compra, v_ID_Producto;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error en el retorno: %. Transaccion cancelada.', SQLERRM;
END $$;