from tkinter import *

ventana = Tk()
ventana.title("Marcos en Tkinter")
ventana.geometry("700x700")


#******************* MARCO Padre 1 ********************
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="CornflowerBlue",
    bd=2,
    relief=SOLID
)
#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco_padre.pack(side=BOTTOM, fill=X, expand=YES)
# Se puede jugar con 'anchor' y 'side'


#******************* MARCO 1 ********************
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=2,
    relief="sunken"
)
#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco.pack(side=LEFT, anchor=SW)
# Se puede jugar con 'side' y 'anchor'; Con side le das la posicion y con anchor la ajustas

#******************* MARCO 2 ********************
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="Crimson",
    bd=2,
    relief=SOLID
)
#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco.pack(side=LEFT, anchor=S)
# Se puede jugar con 'anchor' y 'side'

#******************* MARCO 3 ********************
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="Coral",
    bd=2,
    relief=SOLID
)
#relief => tipo de borde: flat, groove, raised, ridge, solid, sunken. Tambien vale 'relief=SUNKEN'
marco.pack(side=LEFT, anchor=S)
# Se puede jugar con 'anchor' y 'side'



#******************* MARCO Padre 2 ********************
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="Cyan",
    bd=2,
    relief=SOLID
)
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




ventana.mainloop()