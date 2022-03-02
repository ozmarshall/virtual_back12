#hola esto es un comentario
# TODO: Logica para un controlador

edad = 30
 #variable de texto

nombre = "eduardo"
apellido ='de rivero'

# si queremos tener un texto que pueda contener saltos de linea
descripcion = """hola amigos :
como estan? 
yo muy bien jeje"""

descripcion2 = '''hola amigos :
como estan? 
yo muy bien jeje'''

print('a', 'b', 'c')
print(descripcion2)
print(descripcion)

#variables numericas 
year = 2022

#type() = mostrata que tipo de variable es 
print(type(year))
print(type(descripcion))

#variable sin contenido a exepcion del None
#en python None = null | undefined
especialidad = None

print(type(especialidad))
#id da la ubicacion de esa variable en ralcion del dispositivo
print(id(especialidad))

#del elimina la variable de la memoria
del year
print (year)

nombre = 'eduardo100'

print(nombre)

#concatenar 
print('el nombre es :' ,nombre, 'del usuario' )
