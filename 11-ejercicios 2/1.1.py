"""
Ejercicio 1.1
-------------

1- Programa con una lista con 8 numeros enteros 
2- Tiene que recorrela y mostrarla
    2.1- Hacer funcion que devuelva un string
3- Ordenarla y mostrarla
4- Mostrar Longitud
5- Buscar un elemento dentro de la lista

"""
#***** MODO 1 *********
numeros = [1,8,3,2,6,7,4,5]


#***** MODO 2 *********
"""
numeros = []
while len(numeros)<=7:
    num=int(input("Dame un numero: "))
    numeros.append(num)
    num=0
"""


# 2- Recorrer y mostrar
for numero in numeros:
    print(f"{numero}")

print("\n\n")


# crear Funcion que recorra la lista y devuelva un string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado+=str(elemento)
        # print(elemento)
    return resultado
    

print(mostrarLista(numeros))

print("************")

# 3- Ordenar y mostrar
numeros.sort()
for numero in numeros :
    print(numero)

print("************")

# 4- Mostrar longitud
print(len(numeros))

print("************")

# 5- Buscar un elemneto en la lista
print(numeros.index(1))