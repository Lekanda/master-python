"""
                    Ejercicio 2
                    -----------
- Añade valores a una lista mientras la longitud sea menor a 120
- Plus usar "While" y "For"
"""


# Con WHILE
"""
numeros=[]
var=0
while len(numeros) < 120:
    numeros.append(var)
    var+=1
print(numeros)
"""



# Con FOR
numeros=[]
for contador in range(0,120):
    numeros.append(f"Elemento-{contador}")
    print(f"Mostrando el : " + numeros[contador])

print(numeros[22])
    