"""
- Definicion: Los modulos son funcionalidadesya hechaspara reutilizar
- Hay muchos modulos hechos ya: (Python Module Index)

        https://docs.python.org/3/py-modindex.html

- Importamos mi modulo del modulo mimodulo.py en esta misma carpeta
"""



"""
# MODO 1
import mimodulo
print(mimodulo.holaMundo("Andres"))
print(mimodulo.calculadora(2,2,"+"))
"""



# MODO 2: Solo trae la funcion que queremos no todo el modulo
"""
from mimodulo import holaMundo
from mimodulo import calculadora
print(holaMundo("Andres"))
print(calculadora(2,2,"-"))
"""



# MODO 3 : No Quiero solo una funcion , las quiero todas pero para llamar al modulo no quiero escribir:
                # " mimodulo.calculadora(2,2,"+") "
# Trae todas las funciones del modulo y solo tenemos que poner el nombre de la funcion
from mimodulo import *
print(holaMundo("Andres"))
print(calculadora(2,2,"+"))




# MODULO DE FECHAS
import datetime

# Nos da la fecha
print(datetime.date.today())

# Nos da la fecha y hora
fecha_completa= datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.day)
print(fecha_completa.month)
print(fecha_completa.second)

fecha_personalizada = fecha_completa.strftime("%d/%m/%y, /%b/%B/%M/%m/%H/%h")
print(fecha_personalizada)
# En este link estan todos los modificadores de fecha personalizada
                # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())





# MODULO DE MATEMATICAS
import math
# Raiz cuadrada de 10 
print("Raiz cuadrada de 10: ",math.sqrt(10))
#Numero Pi
print("Numero pi: ", math.pi)
print("Numero pi: ", float(math.pi))
# Redondea al alta
print("Redondear: ", math.ceil(6.2369587))
# Redondea a la baja
print("Redondear: ", math.floor(6.2369587))





# MODULO RANDOM (Aleatorio)
import random

print("Numero al azar entre 15 y 100: ", random.randint(15,100))
