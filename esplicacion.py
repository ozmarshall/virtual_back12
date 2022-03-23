def sumar(a, b):
    return a + b

print (sumar(10,5))
print (sumar(a=10, b=5))
parametros = {
    'a': 10,
    'b': 5
}

print(sumar(**parametros))

def restar(**kwargs):
    print (kwargs)

print(restar(x=1, y=2, z=3))