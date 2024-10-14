-- Tabla tocadiscos
CREATE TABLE Tocadiscos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disco VARCHAR(100),
    velocidad INTEGER CHECK(velocidad IN (33, 45, 78)),
    pista_actual INTEGER,
    en_reproduccion BOOLEAN
);

-- Insertar datos 
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco A', 33, 1, 0);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco B', 45, 2, 1);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco C', 78, 3, 0);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco D', 33, 4, 1);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco E', 45, 5, 0);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco F', 33, 6, 1);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco G', 78, 7, 0);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco H', 45, 8, 1);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco I', 33, 9, 0);
INSERT INTO Tocadiscos (disco, velocidad, pista_actual, en_reproduccion) VALUES ('Disco J', 78, 10, 1);

-- Consultas SELECT
-- 1. Obtener todos los registros de la tabla
SELECT * FROM Tocadiscos;

-- 2. Obtener todos los discos que están en reproducción
SELECT disco FROM Tocadiscos WHERE en_reproduccion = 1;

-- 3. Obtener los discos con velocidad de reproducción de 33 RPM
SELECT disco, pista_actual FROM Tocadiscos WHERE velocidad = 33;

-- 4. Contar el número de discos que no están en reproducción
SELECT COUNT(*) AS total_pausados FROM Tocadiscos WHERE en_reproduccion = 0;

-- 5. Obtener todos los discos que están en una pista superior a 5
SELECT disco FROM Tocadiscos WHERE pista_actual > 5;
