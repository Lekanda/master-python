from tkinter import *

ventana = Tk()
ventana.title("Marcos en Tkinter")
ventana.geometry("700x700")


#******************* MARCO Padre 1 ********************
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, fill=X, expand=YES)
# Se puede jugar con 'anchor' y 'side'

#********* MARCO 1  de MARCO Padre 1 ***********
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=2,
    relief="sunken"
)
#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco.pack(side=LEFT, anchor=W)
# Se puede jugar con 'side' y 'anchor'; Con side le das la posicion y con anchor la ajustas
texto = Label(marco, text="Primer marco de prueba")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 9),
    # width=50,
    # height=5,
    # anchor=SE # Tambien se puede poner desde aqui
    bd=3,
    relief=SOLID
)
texto.pack(side=BOTTOM,fill=Y,expand=YES, anchor=SE)
marco.pack_propagate(False) # NO cambia el tamaño de la ventana




#********** MARCO 2  de MARCO Padre 1 ***********
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="Crimson",
    bd=2,
    relief=SOLID
)
#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco.pack(side=RIGHT, anchor=S)
# Se puede jugar con 'anchor' y 'side'


##############################################################


#******************* MARCO Padre 2 ********************
marco_padre = Frame(ventana, width=250, height=250)

#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco_padre.pack(side=TOP, fill=X, expand=YES)
# Se puede jugar con 'anchor' y 'side'


#************* MARCO 1 de MARCO Padre 2**************
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="yellow",
    bd=2,
    relief=SOLID
)
#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco.pack(side=LEFT, anchor=W)
# Se puede jugar con 'anchor' y 'side'

#*********** MARCO 1 de MARCO Padre 2 ***********
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="Coral",
    bd=2,
    relief=SOLID
)
#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco.pack(side=RIGHT, anchor=E)
# Se puede jugar con 'anchor' y 'side'


##############################################################




ventana.mainloop()