# para evitar el salto de linea en una impresion de pantalla print() podemos declarar un parametro end=''
print('hola',end='*')
print('estos son los ejercicios')


# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()

# Escribir una funcion que nosotros le ingresemos el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
# dibujar_octagono()

# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# serie_collatz()


print('ejercicio #1')
filas = int(input("ingrese numero de filas: "))
columnas = int(input("ingrese numero de columnas: "))
print("imprimiendo  un patron con sus datos: ")
for num1 in range(1,filas+1):
    for num2 in range(1,columnas+1):
        print("*", end="")
    print()


print('ejercicio #2')
rombo = int(input('Ingrese su numero para realizar un rombo: '))
def pattern(rombo):
     k = 2 * rombo - 2
     for i in range(0, rombo):
          for j in range(0 , k):
               print(end=" ")
          k = k - 1
          for j in range(0 , i + 1 ):
               print("* ", end="")
          print("\n")
pattern(rombo)







def rombo(n):
    """
    for i in range(1,n+1) -> hacemos un bucle entre el 1 y el numero introducido
    " "*(n-i) -> añade los espacios al inicio
    "*"*(i+i-1) -> por cada valor entre el 1 y n+1, devolvemos la cantidad de asteriscos
    [] -> el resultado lo devuelve dentro de un array
    "\n".join() -> divide el array en una cadena separando cada elemento con un \n (salto de linea)
    """
    result1=[" "*(n-i)+"*"*(i+i-1) for i in range(1,n+1)]
    return "\n".join(result1+list(reversed(result1[:-1])))
 
numero=int(input("indica un numero: "))
print(rombo(numero))