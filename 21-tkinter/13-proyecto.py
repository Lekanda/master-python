"""
                PROYECTO
                --------
- crear un programa que tenga:
    - Una ventana x
    - Tamaño fijo x
    - Ventana no redimensionable x
    -  Un Menu
    - Diferentes pantallas
    - Formulario de añadir productos
    - guardar datos temporalmente
    - MOstrar datos listados en la pantalla 'home'   
    - Opcion de 'Salir'            
"""
from tkinter import *

ventana=Tk()
ventana.geometry("500x500")
ventana.title("Proyecto con TKINTER")
ventana.resizable(0,0)



ventana.mainloop()