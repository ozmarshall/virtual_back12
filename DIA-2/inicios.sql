#hola me llamo Pedro
CREATE DATABASE prueba;
#usamos 
USE prueba;

CREATE TABLE clientes(
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
#dni CHAR(8) UNIQUE,
# VARCHAR(10) UNIQUE

documento VARCHAR(10) UNIQUE,
tipo_documento ENUM('C.E.', 'DNI', 'RUC', 'PASAPORTE', 'C.M.', 'OTRO'),
estado BOOL
);