CREATE TABLE vacunaciones(
     id INT PRIMARY KEY AUTO_INCREMENT,
     nombre VARCHAR(100) UNIQUE NOT NULL,-- nombre que no se pueda repetir y que no admita valores vacios
     estado BOOL DEFAULT TRUE,-- ESTADO estado que solo acepte bools 
     fecha_venc DATE, -- fecha de vencimeibnto date
     procedencia ENUM('USA', 'CHINA', 'RUSIA', 'UK'),-- procedencia sus valorew pueden ser USA, CHINA, RUSIA, UK
     lote VARCHAR(10)-- lote no puede superar los 10 caracteres
); 
-- RENAME TABLE vacunaciones TO vacunas;
CREATE TABLE vacunatorio (
     id INT PRIMARY KEY AUTO_INCREMENT,
     nombre VARCHAR(100) UNIQUE NOT NULL,
     latitud FLOAT,
     longitud FLOAT,
     direccion VARCHAR(200),
     horario_atencion VARCHAR(100),
     -- la llave foranea (FK foreinger key) es la reepresntaciuon de la relacion entre la otra tabla e indicara todo su contenido
     -- representando solo por suy id
     vacuna_id INT,
     FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);

RENAME TABLE vacunatorio TO vacunatorios;

-- DROP elimina la tabla y su contenido a diferencia del DELETE quw solo elimina el contyendido
-- DROP TABLE vacunatorios;
-- DROP DATABASE prueba;

ALTER TABLE vacunatorios DROP COLUMN latitus;
ALTER TABLE vacunatorios ADD COLUMN imagen VARCHAR(100) DEFAULT 'imagen.png' AFTER  horario_atencion;

ALTER TABLE vacunatorios RENAME COLUMN imagen TO foto;
-- ALTER TABLE vacunatorios MODIFY COLUMN imagen INT UNIQUE NOT NULL;

-- un vcacunatorio podra tener uha sola vacuna pero una vacuna puede estar presente en varios vacunatorios
-- vacunas < vacunatorios

-- para ver lo que se ah creado, lka tabla  es con DESC clientes
DESC clientes;
DESC vacunatorios;
