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