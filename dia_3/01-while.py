#><

numero = 0
while numero <= 10:

    #pass 
    print(numero)

    numero += 1

else:
    print('el while termino')



numeros = [1, 5, 16, 28, 234, 67, 29] 
  
even_countador, odd_countador = 0, 0
  
for num in numeros: 
      
    
    if num % 2 == 0: 
        even_countador += 1
  
    else: 
        odd_countador += 1
          
print("numeros pares: ", even_countador) 
print("numeros impares: ", odd_countador)



posicion = 0
par, impar = 0 , 0
while posicion < len(numeros):
    if numeros[posicion] % 2==0:
        par += 1
    else:
        impar += 1
    posicion += 1

print('hay {} numeros pares'.format(par))
print('hay {} numeros impares'.format(impar))

