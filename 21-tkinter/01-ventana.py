"""
TKINTER => Modulo para crear interfaces graficas de usuario
"""
# Importamos todo de
from tkinter import *
import os.path

 # ********Crear la ventana raiz********
ventana = Tk()

#Titulo de la Ventana
ventana.title("Interfaz grafica con PYTHON y TKINTER")

# Comprobar si existe un archivo
ruta_icono = os.path.abspath('./imagenes/Star.ico')
# print(f"Ruta icono : {ruta_icono}")

# 
if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/Star.ico')

# Icono de la ventana
ventana.iconbitmap(ruta_icono)

# Mostrar texto en el programa
texto = Label(ventana, text=ruta_icono)
texto.pack()



# Cambiar el tamaño de la ventana
ventana.geometry("750x450") # Redimensiona (Ancho x Alto)
# Bloquear el redimensionado de ventana
ventana.resizable(0,0) 
    # (0,0) no deja cambiar el tamaño
    # (1,1) deja cambiar el tamaño
    # (1,0) deja cambiar el tamaño de ancho pero no del alto
    # (0,1) deja cambiar el tamaño de alto pero no del ancho



 # Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
