"""
*** Funciones y Metodos para las listas ***
-------------------------------------------

- Ordena
- Añadir Elementos
- Eliminar Elementos
- Dar la vuelta
- Buscar dentro de una lista 
- Contar Elementos
- Cuantas veces aparece una elemento en la lista
- Unir Listas

--------------------------------------------
"""

cantantes= ['Van morrison', 'Neil Young', 'Ottis Redding', 'David Bowie', 'Johny Cash']

numeros = [1,7,3,9,5,6,2,8,10,4]

# *** Ordena los numeros ***
print(numeros)
numeros.sort()
print(numeros)

# *** Añadir Elementos ***

# En este codigo guarda siempre en la ultima posicion del index. Sí se mete otro lo pone encima
cantantes.append("Mikel Laboa")
print(cantantes)
# Mete en la posicion 6 el artista
cantantes.insert(6,"Andres Calamaro" )
print(cantantes)


# *** Eliminar elementos ***
cantantes.pop(1)
cantantes.remove('Mikel Laboa')
print(cantantes)


# *** Dar la vuelta ***
print(numeros)
numeros.reverse()
print(numeros)



# *** Buscar dentro de una lista ***
# Da true si es correcto
print('Andres Calamaro' in cantantes)




# *** Contar Elementos ***
print(len(cantantes))



# *** Cuantas veces aparece un elemento en la lista ***
numeros.append(8)
print(numeros.count(8))



# *** Conseguir un indice ***
print(cantantes.index("Andres Calamaro"))


# *** Unir Listas ***
cantantes.extend(numeros)
print(cantantes)
