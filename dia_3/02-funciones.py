def sumar ( num1, num2):
    print ('se realizara la sumatoria....')
    print (num1 + num2)
sumar(5,7)



def nombre(x):
    '''funcion que recibe un string y lo imprime por consola'''
    print(x)

nombre('pedro')

print(nombre.__doc__)


usuario= []
def registrar(nombre, email, telefono):
    usuario.append({
        'nombre': nombre,
        'email': email,
        'telefono': telefono
    })

    return {
        'message': 'usuario regitrado todo ok',
        'usuario': usuario[0]
    },1,True

resultado, numero, booleano= registrar ('pedro', 'pollo@gmail.com', '909090909')
print(resultado)
print(numero)
print(booleano)

productos=[]

def registrar_productos(nombre, precio, estado=True, almacen='alamcen del centro'):
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'estado': estado,
        'almacen': almacen
    })

    return 'producto agregado exitosamente'

registrar_productos('tomate', 4.5)
registrar_productos('apio', 1.4, False)
registrar_productos('cebolla', 5.34, True)
registrar_productos(nombre='pollo', precio='5.6', estado=True, almacen='almacen de la costa')




def alumnos(clase,*args):
    print(args)

alumnos('pedro', 'juan', 'luis', 'rodrigo', 'liam', )
alumnos('coco', 'daany', 'joshua')
alumnos('mario')
alumnos('martha', 30, False, 'juan', 1.5)

def ingresarProducto(**kwargs):
    print(kwargs)
    if(kwargs.get('nombre')):
        print('el usuario quiere agregar un nombre')
    if(kwargs.get('cantidad')):
        print('el usuario quiere agregar la cantidad de producto')


ingresarProducto(nombre='manzana', precio=2.1, estado=True, pais_procedencia='peru')
ingresarProducto(tamanio='grande', cantidad=100, nombre='pera de agua')




def saludar_n_veces(limite):
    if(limite == 0):
        return 'llegue al limite'
    print('saludar')
    return saludar_n_veces(limite-1)

resultado = saludar_n_veces(10)
print(resultado)





def factorial(limite):
    if limite == 0:
        return 1

    return limite * factorial(limite -1)

resultado = factorial(0)
print('la factorial es : ',resultado)


nombre_persona = 'maria '
origen_persona = 'cuzco'

def duda(nombre, origen):
    if nombre_persona == 'maria' and origen_persona == 'arequipa':
        return 'me caso '
    else: 
        return 'next'
resultado = 'me caso ' if  nombre_persona == 'maria' and origen_persona == 'arequipa' else 'next'
resultado2 = duda('maria', 'arequipa')

print(resultado)
print(resultado2)



cuadrado = lambda numero: numero ** 2
sacar_igv = lambda precio: precio * 0.18

rpta = cuadrado(4)

precio_sin_igv = sacar_igv(100)
print(rpta)
print(precio_sin_igv)

precio_sin_igv = sacar_igv(50)
print(precio_sin_igv)





