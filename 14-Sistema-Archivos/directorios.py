import os, shutil

# CREAR una carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# ELIMINAR carpeta
# os.rmdir("./mi_carpeta")

# COPIAR una Capeta
"""
ruta_original="./mi_carpeta"
ruta_nueva="./mi_carpeta_COPIADA"

shutil.copytree(ruta_original,ruta_nueva)
"""

# ELIMINAR carpeta copiada
# os.rmdir("./mi_carpeta_COPIADA")



# LISTAR los archivos de una carpeta
print("Contenido de la carpeta")
contenido = os.listdir("./mi_carpeta")
# print(contenido)

for fichero in contenido:
    print("Fichero: "+ fichero)
