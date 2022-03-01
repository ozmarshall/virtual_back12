#operadores de comparacion
numero1, numero2 = 10, 20

#igual que 
print (numero2==numero1)

#mayor que | mayor igual que
print (numero2>numero1)
print (numero2>=numero1)

#menor que | menor igual que 
print (numero2<numero1)
print (numero2<=numero1)


#diferente de
print (numero2!=numero1)

#operadores logicos
print((10>5)and(10<5))
print((10>5)and(30<20))

#operadores de identidad
#is
#is not
#sirve para ver si estan apuntando a la misma direccion de memoria
verduras = ['apio', 'lechuga', 'zapallo']
verduras2 = verduras
verduras3 = ['apio', 'lechuga', 'zapallo']

verduras2[0] ='perejil'
verduras2[1] ='manzana'

verduras4 = verduras.copy()
verduras4[0] = 'huacatay'
print(verduras2 is verduras)
print(verduras)
print(verduras2)
print(verduras3 is verduras)

print ('la posicion de la variable verduras es :', id(verduras))
print ('la posicion de la variable verduras2 es :', id(verduras2))
print ('la posicion de la variable verduras4 es :', id(verduras4))

nombre = 'eduardo'
nombre2 = nombre
print(nombre2 is nombre)
print(id(nombre2))
print(id(nombre))
nombre2= 1
print(nombre)
print(id(nombre2))
print(id(nombre))

nombre = 'eduardo'
nacionalidad = 'venezolano'
print (nombre == 'eduardo' and (nacionalidad == 'peruano' or nacionalidad == 'colombiano'))
