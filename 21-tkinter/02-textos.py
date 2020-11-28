from tkinter import *


ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg="red", # Color Letra
    # bg="Black", # Color fondo del texto
    bg="#122523", # Color fondo del texto
    padx=50, # Margen en el eje X
    pady=20, # Margen en el eje Y
    font=("Consolas", 30) # Tamaño de la funte de texto
)
texto.pack()

texto = Label(ventana, text = "Hola soy el programador")
texto.config(
    # justify=RIGHT, # Justifica , pero solo sobre el texto, no se nota
    # width=600,
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10, # Margen en el eje X
    pady=10, # Margen en el eje Y
    cursor="spider" # Al poner el raton encima de este elemento cambia el simbolo del Raton: circle, arrow, clock, spider
)
texto.pack(anchor=SE)

ventana.mainloop()