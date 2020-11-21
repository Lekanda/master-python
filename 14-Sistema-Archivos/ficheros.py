from io import open
import pathlib




# Abrir archivo
ruta=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")


# Escribir dentro del archivo
archivo.write("*****HOLA desde python********\n")


# CLOSE Crerra el archivo. ¡¡SIEMPRE!! hay que cerrar los archivos
archivo.close()