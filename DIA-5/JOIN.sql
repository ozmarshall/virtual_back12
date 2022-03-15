USE prueba;

SELECT * 
FROM vacunatorios INNER JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id = 1;

-- LEFT JOIN 
-- traera todo el contenido de la tabla de la iz y adicionalmente el contenido de interseccion
-- con la tabla de la derecha

SELECT * 
FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;

INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
                         ('POSTA JOSE GALVEZ', 14.26598, 32.2569, 'AV. EL SOL 755', 'LUN-VIE 15:00 22:00', null, null);
                         
SELECT * 
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;

-- FULL OUTER JOIN
-- trae toda la info tandoi de la tabla y la izquierda

SELECT * 
FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id UNION
SELECT * 
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;

SELECT vacunas.nombre, vacunatorios.nombre
FROM vacunatorios JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre = 'Pfizer';

SELECT vacu.nombre, vac.nombre
FROM vacunatorios AS vac JOIN vacunas AS vacu ON vac.vacuna_id = vacu.id
WHERE vacu.nombre = 'Pfizer';

SELECT * FROM vacunatorios;


-- 1. Devolver todos los vacunatorio en los cuales la vacuna sea Sinopharm y su horario de atencion sea de LUN-VIE
SELECT * 
FROM vacunatorios JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre = 'SINOPHARM' and horario_atencion LIKE '%LUN-VIE%';


-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latitud -5.00 y 10.00 IN()


-- 3. Devolver todas las vacunas que no tengan vacunatorio y solamente su procedencia y nombre
SELECT procedencia, vacunas.nombre
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id IS NULL;

