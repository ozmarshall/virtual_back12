-- INSERTAR DATA 
USE prueba;
INSERT INTO vacunas (nombre, estado, fecha_vencimiento, procedencia, lote) VALUES
                    ('PFIZER', true, '2022-08-16', 'USA', '123jkl'),
                    ('SINOPHARM', true, '2022-10-10', 'CHINA', 'vxcvxc'),
                    ('MODERNA', true, '2022-09-14', 'USA', 'zxczxc'),
                    ('SPUTNIK', false, '2022-10-04', 'RUSIA', 'ghjkhjfg');
                    
INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
                        ('CAMINO REAL', 14.121, -21.121, 'AV GIRASOL 115', 'LUN-VIE 07:00 - 15:00', null, 1),
                        ('HOSP. GNRAL.', 17.521, 11.1891, 'AV CIRCUNVALACION S/N', 'LUN-VIE 07:00 - 15:00', 'hospital.jpg', 2),
                        ('POSTA CERRO AZUL', 11.258, 67.447, 'AAHH LOS QUERUBINES LOTE 3 MZ J', 'LUN-SAB 07:00 - 15:00', 'foto01.png', 1),
                        ('ESTADIO LOS PALITOS', 24.121, -21.121, 'CALLE ESPINOSA 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'est0001.jpg', 3),
                        ('PLAZA DEL AMOR', 4.116, -21.121, 'AV DE LOS HEROES ANONIMOS S/N', 'LUN-VIE 07:00 - 15:00', null, 1);
                        
-- ALTER TABLE vacunas RENAME COLUMN fecha_venc TO fecha_vencimiento;

-- 1.- mostrar todos los nombres de las vacunas
SELECT nombre FROM vacunas;

-- 2.- mostrar todas las vacunas que sean de preocedencia de usa 
SELECT * FROM vacunas WHERE procedencia = 'USA';

-- 3.- mostrar las vacunas que no sean de procedencia usa 
SELECT * FROM vacunas WHERE NOT procedencia = 'USA';

-- 4.- mostrra las vacunas que en su lote tengan los digitos 'xc'
SELECT * FROM vacunas WHERE nombre LIKE '%xc%';

-- 5.- mostrar todos los vacunatorios que tengan horario de atencion los dias miercoles
SELECT * FROM vacunatorios WHERE horario_atencion LIKE '%MIE%' 
                                                    OR horario_atencion LIKE '%LUN-VIE%' 
                                                    OR horario_atencion LIKE '%LUN-SAB%'; 

-- 6.- mostrar todos os vacunatorios que tengan la vacuna_id 1 pero que tengan foto
SELECT * FROM vacunatorios WHERE vacuna_id = 1 AND foto IS NOT NULL;



                        