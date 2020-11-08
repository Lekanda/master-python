nada = None
cadena = "Hola soy Andres"
entero=99
flotante=9.8
booleano= True
lista=[1,2,3,4,5,6,7]
listaStrings= ["hola mundo", 45, "true"]
tuplaNoCambia= ("master", "en", "Python")
diccionario = { # Parecido al JSON
    "nombre":"Andres",
    "apellidos":"Bernaola",
    "curso":"Master Python"
}
rango=range(9)
dato_byte = b"Probando" # Esa b indica que es de tipo byte






# imprimir variable
# Tipo NONE
print(nada)
print(type(nada)) # Da el tipo de dato
# Tipo STR string
print(cadena)
print(type(cadena))
# Tipo Enteros INT
print(entero)
print(type(entero))
# Tipo flotante FLOAT
print(flotante)
print(type(flotante))
# Tipo booleano BOOL
print(booleano)
print(type(booleano))
# Tipo lista,array LIST
print(lista)
print(type(lista))
# Tipo LIST variados
print(listaStrings)
print(type(listaStrings))
# Tipo tupla TUPLE . No cambian los datos
print(tuplaNoCambia)
print(type(tuplaNoCambia))
# Tipo diccionario DICT
print(diccionario)
print(type(diccionario))
# Tipo rango RANGE. Desde 0 a 9
print(rango)
print(type(rango))
# Tipo byte BYTES
print(dato_byte)
print(type(dato_byte))

# Cap 12

texto = "Hola soy Andres"
numerito= 999

# Solo se pueden concatenar del mismo tipo, sí no da error
# Para convertir uun dato INT a STR se hace
numerito= str(999)
# con los demas es igual: float, etc
print(texto + " " + numerito)

