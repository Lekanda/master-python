from io import open
import pathlib
import shutil



# Abrir archivo
ruta=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")


# Escribir dentro del archivo
archivo.write("*****HOLA desde python********\n")


# CLOSE Cierra el archivo. 
#           "¡¡SIEMPRE!! hay que cerrar los archivos"
archivo.close()


# Abrir archivo para LEER
ruta=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo_lectura = open(ruta, "r")
# Leer contenido del archivo abierto
# contenido= archivo_lectura.read()
# print(contenido)# Lee por lineas
# for elemento in contenido: # Lee con caracter
#     print(elemento)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
# print(lista)
for elemento in lista: # Lee con caracter
    print(elemento)

for frase in lista:
    lista_frase = frase.split() # Crea una lista con cada elemento
    print(lista_frase)
    # print("-"+frase.capitalize())



# Copiar un archivo. UTILZAMOS "SHUTIL"
"""
ruta_original=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva=str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa="../07-Ejercicios/fichero_copiado_prueba55.txt"
# ruta_alternativa2=str(pathlib.Path().absolute())+"/../07-Ejercicios/fichero_copiado_prueba2.txt"
# print(ruta_alternativa2)
shutil.copyfile(ruta_original,ruta_alternativa)
"""

# Mover
"""
ruta_original=str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva=str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original,ruta_nueva)
"""



# ELIMINAR un archivo
import os
"""
ruta_nueva=str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""





# Comprobar sí existe
import os.path
# Para coger una ruta de un archivo
print(os.path.abspath("/"))
print(os.path.abspath("./"))
print(os.path.abspath("../"))
# Una forma de hacerlo
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
# Otra forma de hacerlo
ruta_comprobar="./fichero_texto.txt"
print(ruta_comprobar)
if os.path.isfile(ruta_comprobar):
    print("El fichero existe")
else:
    print("El fichero no existe")