"""
                PROYECTO
                --------
- crear un programa que tenga:
    - Una ventana (X)
    - Tamaño fijo (X)
    - Ventana no redimensionable (X)
    - Un Menu superior (Inicio,Añadir, Informacion, Salir) (X)
    - Diferentes pantallas 
    - Formulario de añadir productos
    - guardar datos temporalmente
    - MOstrar datos listados en la pantalla 'home'   
    - Opcion de 'Salir' (X)       
"""
import tkinter as TK
# definir ventana
ventana=TK.Tk()
ventana.geometry("500x500")
ventana.title("Proyecto con TKINTER")
ventana.resizable(0,0)


# Pantallas
def home():
    # Montar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)
    # Ocultar otras Pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True


def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)
    # Ocultar otras Pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True


def info():
    
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1,column=0)
    # Ocultar otras Pantallas
    home_label.grid_remove()
    add_label.grid_remove()
    return True


# Definir campos de Pantallas(INICIO/HOME)
home_label=TK.Label(ventana, text="Inicio")
# Definir campos de Pantallas(ADD)
add_label=TK.Label(ventana, text="Añadir producto")
# Definir campos de Pantallas(INFO)
info_label=TK.Label(ventana, text="Informacion")
data_label=TK.Label(ventana, text="Creado por Andres Bernaola")


# Cargar la pantalla de inicio
home()


# Menu Superior
menu_superior=TK.Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)
# Cargar el menu superior
ventana.config(menu=menu_superior)


#Cargar ventana
ventana.mainloop()