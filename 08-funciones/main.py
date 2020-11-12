"""
Funcion: Un conjunto de instrucciones agrupadas en un nombre

def nombreFuncion(parametros):
    # Bloque de codigo 


# Para invocar a la funcion
nombreFuncion(parametro/s)

"""

# Ejemplo 1
nombre=input("dame un nombre: ")
print("\n")
print("########## EJEMPLO1 ##########")
print("\n\n")

def muestraNombres(nombre):
    print("Andres")
    print("Bernaola")
    print(f"hola {nombre}")
    print("\n\n")

muestraNombres(nombre)

# Ejemplo 4 PARAMETROS OPCIONALES
"""
-Sí queremos que uuno de los argumentos de la funcion sea opcional:
 def empleado(nombre, dni=False o numero por defecto, None)

 -Se puede poner un if en el interior para que no lo haga

 if dni!=None:   lo hace

 -O pasar la 2ªvariable en el llamamiento de la funcion
"""

