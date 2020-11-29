from tkinter import *


ventana = Tk()
# ventana.geometry("700x500")


#**********VENTANA 1*******************
texto = Label(ventana, text = "Curso python")
texto.config(
    fg="green", # Color Letra
    bg="Black", # Color fondo del texto
    # bg="#122523", # Color fondo del texto
    padx=10, # Margen en el eje X
    pady=10, # Margen en el eje Y
    font=("Consolas", 30) # Tamaño de la funte de texto
)
texto.pack(side=TOP, fill=X, expand=YES)


#**********VENTANA 2*******************
texto = Label(ventana, text = "Basico 2")
texto.config(
    fg="green", # Color Letra
    # bg="Black", # Color fondo del texto
    bg="#122523", # Color fondo del texto
    padx=10, # Margen en el eje X
    pady=10, # Margen en el eje Y
    font=("Consolas", 10) # Tamaño de la funte de texto
)
texto.pack(side=LEFT, fill=X, expand=YES)
# fill=X y expand=YES => expande el cuadro del texto hasta rellenar la ventana. El fill indica que rellena en x y expand para expandir



#**********VENTANA 3*******************
texto = Label(ventana, text = "Basico 3")
texto.config(
    fg="green", # Color Letra
    # bg="Black", # Color fondo del texto
    bg="#630021", # Color fondo del texto
    padx=10, # Margen en el eje X
    pady=10, # Margen en el eje Y
    font=("Consolas", 10) # Tamaño de la funte de texto
)
texto.pack(side=LEFT, fill=X, expand=YES)



#**********VENTANA 4*******************
texto = Label(ventana, text = "Basico 4")
# si igualamamos los parametros con datos que se pasan a la funcion 'pruebas' no hace falta seguir un orden a la hora de declarar los parametros como esta en el ejemplo. Esto es util cuando hay muchos parametros que pasar
texto.config(
    # justify=RIGHT, # Justifica , pero solo sobre el texto, no se nota
    # width=600,
    # height=3,
    bg="green",
    font=("Consolas", 10),
    padx=10, # Margen en el eje X
    pady=10, # Margen en el eje Y
    cursor="spider" # Al poner el raton encima de este elemento cambia el simbolo del Raton: circle, arrow, clock, spider
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()