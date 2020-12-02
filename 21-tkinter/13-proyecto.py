"""
                PROYECTO
                --------
- crear un programa que tenga:
    - Una ventana (X)
    - Tamaño fijo (X)
    - Ventana no redimensionable (X)
    - Un Menu superior(Inicio,Añadir, Informacion, Salir) (X)
    - Diferentes pantallas
    - Formulario de añadir productos
    - guardar datos temporalmente
    - MOstrar datos listados en la pantalla 'home'   
    - Opcion de 'Salir' (X)       
"""
from tkinter import *
# definir ventana
ventana=Tk()
ventana.geometry("500x500")
ventana.title("Proyecto con TKINTER")
ventana.resizable(0,0)


# Menu Superior
menu_superior=Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="Informacion")
menu_superior.add_command(label="Salir", command=ventana.quit)
# Cargar el menu superior
ventana.config(menu=menu_superior)




#Cargar ventana
ventana.mainloop()