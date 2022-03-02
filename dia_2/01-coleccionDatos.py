#coleccion de datos es una variable que puede almacenar varios valores
#listas (List)
#ordenadas y que puede ser modificada

nombre= ['pedro', 'luis', 'cesar']
combinada= ['eduardo', 80, 15, 20.8, 'pedro', [1,2,3]]

#las listas siempre comienzan en la posicion 0
print(nombre[0])

#cuando hacemos e uso de valores n en una lsita internamete python le dara vuelta
print(nombre[-1])

print(nombre)
#si queremos ingresar a una posicion inexsitente nos lanzara un error de indice fuera de rango
#print(nombre[10])

#poc () > remuieve el ultimo elemento de la lista y se puede almacenar en otra variable
resultado = nombre.pop()
print (resultado)
print(nombre)

#append() > ingresa un nuevo elelmento a la ultima posicion de la lista
nombre.append ('juancito')

#elimina el contenido de una posicion de la lsita pero no lo podemos almacenar en otra variable
del nombre[0]
print(nombre)

# clear () > limpia toda la lista y la deja como nueva
nombre.clear () # > []
print(nombre)

x=combinada[:]
y=combinada

# indica una subseleccion demla lista
print(combinada[1:4])

# indicando el contenido de la lsita y esto es muyu uitil para hacer una copia d ela lsuta sin usar su misma posicion de memoria
print (combinada[:])
print(id(x))
print(id(combinada))
print(id(y))

#desde el inicio hasta el 2
print(combinada[:2])

#desde la posicion 2 hasta el final
print(combinada[2:])

meses_dscto= ['enero', 'marzo', 'julio']
mes = 'septiembre'
mes2='enero'
#indicara si el valor no se encuentra dentro de la lista

print(mes not in meses_dscto)
#indicar si el valor s encuantre en la liksta
print(mes2 in meses_dscto)

seccion_a=['rozana', 'juan']
seccion_b=['julia', 'martin']
#si hacemos la sumatoria en las listas estas se combianaran en la cual la segunda lista ira despues de la prinmewra
print(seccion_a+seccion_b)

#sirve para esperar un dato ingredado por el usuario
dato= input('ingrersa un nombre:')
print(dato)

#tuplas
#muy similar a la lsita a excepcion que no se puede modificar
cursos = ('back', 'front')

print(cursos)
print(cursos[0])
print(cursos[0:1])
#cursos.append('otra cosa')
#cursos[0]= 'mobile design'

variada= (1,2,3, [4,5,6])
variada [3][0]= 'hola'

print(variada)
#creamos una nuevas lsita a raiz de una tupla llmando a la clase li

print (2 in variada)
print (1 not in variada)
print ('1' not in variada)

variada_lista=list(variada)
list((1,2,3)) #[1,2,3]

print (variada_lista)

# para ver el tamano de una tupla o una lista
print(len(variada_lista))


#conjuntos
#coleccion de datos desordenada una vez que se crea, ya no se accede a las posicones de sus elemtos 
estaciones = {'verano', 'otonio', 'primavera', 'invierno'}
print(estaciones)
print(estaciones)
print ('invierno'  in estaciones)
estaciones.add('otro')
estacion=estaciones.pop()
print(estacion)


#dicionarios
persona={
    'nombre': 'pedro',
    'app': 'ram',
    'correo': 'pollo@gmail.com'
}

print(persona['app'])
print(persona.get('app', 'no hay no existe'))
print(persona.keys())
print(persona.values)
print(persona.items)

persona['edad']=28
persona['nombre']='ximena'
print(persona)

persona.pop('app')







