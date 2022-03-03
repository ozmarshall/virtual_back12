#if -else
edad= int(input('ingresa tu edad '))

if (edad > 18): 
    print('la persona es mayor de edad')
    print('otra impresion')


elif edad > 15 :
    print('puedes ingresar ala preparatoria')
else:
    print('eres chibolo')
print('finalizado')



#elif
edad= int(input('ingresa tu edad '))

if (edad > 18): 
    print('la persona es mayor de edad')
    print('otra impresion')

else: 
    print('eres menor de edad')

print('finalizado')



ingreso= int(input('ingresa tu ingreso mensual '))

if (ingreso > 500): 
    print('usted no recibe bono')

elif ingreso >= 250 and ingreso <=500 :
    print('usted recibe bono')

else: 
    print('usted recibe bono')

print('finalizado')

