"""

"""

nombre="AnDres"

# Funciones Generales
print(nombre)
print(type(nombre))

# Detectar el tipado
comprobar= isinstance(nombre, str) 
    # True si lo que hay en "nombre" es "str"
    # isistance => Comprueba si es del tipo que queremos
print(comprobar)

# Limpiar espacios en un str, antes y despues de la cadena
frase="     hola me llamo Andrés         "
print(frase)
print(frase.strip())

# Eliminar Variables
year=2020
print(year)
del year
# print(year)

#Comprobar variables vacias
texto= "  ff "
# texto= ""

if len(texto)<=0 :
    print("La variable esta vacia")
else:
    print("La variable esta llena", len(texto))


# Encontrar caracteres en un STR
frase="La vida es bella"

print(frase.find("vida"))

# Reemplazar palabras en un STR
nuevafrase=frase.replace("vida", "casa")

print(nuevafrase)


## Procesar Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())

