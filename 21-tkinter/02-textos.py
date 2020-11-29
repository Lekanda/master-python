from tkinter import *


ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg="green", # Color Letra
    # bg="Black", # Color fondo del texto
    bg="#122523", # Color fondo del texto
    padx=50, # Margen en el eje X
    pady=20, # Margen en el eje Y
    font=("Consolas", 30) # Tamaño de la funte de texto
)
texto.pack(anchor=E)

def pruebas(nombre,apellidos,pais):
    return f"Hola {nombre} {apellidos} eres de {pais}"

texto = Label(ventana, text = pruebas(pais="Espña",nombre="Andres", apellidos="Bernaola", ))
# si igualamamos los parametros con datos que se pasan a la funcion 'pruebas' no hace falta seguir un orden a la hora de declarar los parametros como esta en el ejemplo. Esto es util cuando hay muchos parametros que pasar

texto.config(
    # justify=RIGHT, # Justifica , pero solo sobre el texto, no se nota
    # width=600,
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10, # Margen en el eje X
    pady=10, # Margen en el eje Y
    cursor="spider" # Al poner el raton encima de este elemento cambia el simbolo del Raton: circle, arrow, clock, spider
)
texto.pack(anchor=SE)

ventana.mainloop()