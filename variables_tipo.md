### Variables y Tipos
##### Variables
```python
# Ejemplo 1***
texto = "Master en Python"
print(texto)


# Ejemplo 2***
texto = "Master en Python"
texto = 1
print(texto)

# Ejemplo 3***
texto = "Master en Python"
texto2 = "con Victor Robles"
num=45
print(texto)
print(texto2)
print(num)

# Ejemplo 1***
texto = "Master en Python"
texto2 = "con Victor Robles"
texto3 = "de Udemy"
web= "www.ok.com"

    

# Es lo mismo
print(texto + " " + texto2 + " " + texto3 + " - " + web)
print(f"{texto} {texto2} {texto3} - {web}")

# Esta puede que sea la mejor
web2= f"www.ok.com {texto2}"
print(f"{texto} {texto2} {texto3} - {web2}")

# Otra forma
print("Este es el curso {} {} {}".format(texto,texto3,texto2))


print(texto, texto2, texto3)
```

##### Tipos
```python
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
```

##### Curiosidades
```python
mi_texto = "'Master'"
mi_texto2 = "en Python"

# el guion normal no es valido, solo el guion bajo

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

# Para poner comillas en un texto y que lo imprima  \"  \"   
mi_texto2 = "en \"Python\""
texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

# Con comilla simple si la pone directamente
# \n => salto de linea
# \t => salto de tabulador
# \r => Borra lo que hay detras de esa \r
```