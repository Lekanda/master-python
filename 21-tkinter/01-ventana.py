"""
TKINTER => Modulo para crear interfaces graficas de usuario
"""
# Importamos todo de
from tkinter import *

 # ********Crear la ventana raiz********
ventana = Tk()

#Titulo de la Ventana
ventana.title("Interfaz grafica con PYTHON y TKINTER")


# Cambiar el tamaño de la ventana
ventana.geometry("750x450") # Redimensiona (Ancho x Alto)
# Bloquear el redimensionado de ventana
ventana.resizable(0,0) 
    # (0,0) no deja cambiar el tamaño
    # (1,1) deja cambiar el tamaño
    # (1,0) deja cambiar el tamaño de ancho pero no del alto
    # (0,1) deja cambiar el tamaño de alto pero no del ancho

# Icono de la ventana
ventana.iconbitmap("./imagenes/Star.ico")

    






 # Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
