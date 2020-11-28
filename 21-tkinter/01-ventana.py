"""
TKINTER => Modulo para crear interfaces graficas de usuario
"""
# Importamos todo de
from tkinter import *
import os.path

class Programa:

    def __init__(self):

        self.title = "Interfaz grafica con PYTHON y Tkinter"
        self.icon = './imagenes/Star.ico'
        self.icon_alt = './21-tkinter/imagenes/Star.ico'
        self.size = "770x470"
        self.resizable = False

    def cargar(self):

        #######################################
        # ********Crear la ventana raiz********
        #######################################
        ventana = Tk()
        self.ventana = ventana
        #Titulo de la Ventana
        ventana.title(self.title)
        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)
        print(f"Ruta icono : {ruta_icono}")

        # Sí la ruta es difente a 'ruta_icono' : cambio de la ruta en 'ruta_icono'
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)
            print(f"Ruta icono : {ruta_icono}")

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Cambiar el tamaño de la ventana
        ventana.geometry(self.size) # Redimensiona (Ancho x Alto)
        # Sí resizable es 'True'
        if self.resizable:
            ventana.resizable(1,1)
        else: 
            ventana.resizable(0,0)
        # (0,0) no deja cambiar el tamaño
        # (1,1) deja cambiar el tamaño        
         # (1,0) deja cambiar el tamaño de ancho pero no del alto       
        # (0,1) deja cambiar el tamaño de alto pero no del ancho
        
        # Arrancar y mostrar la ventana hasta que se cierre la ventana
        # ventana.mainloop()

    def addTexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre la ventana
        self.ventana.mainloop()


# Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola como estas??")
programa.addTexto("La lluvia en Sevilla es una maravilla")
programa.mostrar()

# Para cambiar la forma en que se ejecuta el archivo, es dcir, para que solo ejecute la ventana sin python por detras. Cambiaremos la extension a .pyw