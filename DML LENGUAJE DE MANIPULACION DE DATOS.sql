USE prueba;

-- SUB parte de SQL:
-- DML: data manipulation language(lenguaje de manipulacion de datos)
-- se utiliza para la mnaipulacion de la infoirmacion de una base de datos
-- INSERT, SELECT, UPDATE, DELETE

INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
			         ('pedro', '12121212', 'DNI', true);
                     
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
			         ('pepe', '19876212', 'DNI', true),
                     ('juan', '1976523412', 'ruc', false);
                     
-- SELECT : es el comando que sirve para visualizar la informacion de una detrminada tabla 
-- SELECT col1, col2,....FROM tabla;

SELECT nombre, documento FROM clientes;

-- si queremos observar todas las columnas de esta tabla


    -- WHERE col_nombre = valor> <>= <=
    -- al usar parentesis en una condicional hara que eesa condiciones internas se ejecuten primero
    -- para luego recien el resultado se comnpare con la condicion externa
SELECT * FROM clientes WHERE documento = '12121212' AND (nombre = 'pedro' OR nombre = 'juan');

-- seleccionar a todas las personas que tienbes dni y que su estado sea true
SELECT * FROM clientes WHERE tipo_documento = 'DNI' AND estado = true;

-- LIKE en columnas de string para hacer una similitud y ademas usartemos los % para indicar si no se sabe
-- en que parte exactamente esta esa letra o letras
SELECT * FROM clientes WHERE nombre LIKE '%uan%';
SELECT * FROM clientes WHERE nombre LIKE '%ed%o';

-- UPDATE sirve para actualizar uno o varios registros de una determioanda tabla
-- UPDATE tabla SET col=nuevo_valor, .... WHERE col=val;
UPDATE clientes SET  nombre = 'periquito', documento = '54545434' WHERE id =242424 AND nombre = 'pedro';

-- modeo seguro > es el modo que nos impoide hacer actualizaciones (UPDATE) y eliominamos (DELETE) sinn usar
-- una col que sea indique (o PK)
-- otra forma de acceder mediante el workbench es en el menu Edit > preference > SQL Editor y al final estara la 
-- opcion para modifcar
-- para desactivar el modo seguro:

SET SQL_SAFE_UPDATES = false;

-- DELETE sirve para eliminar REGISTROS
DELETE FROM clientes = 

