from tkinter import *


ventana = Tk()
ventana.geometry("800x500")



encabezado=Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas",20)
)
encabezado.grid(row=0,column=0,columnspan=5,sticky=W)

def mostrarProfesion():
    texto=""
    if web.get(): # Sí me da True
        texto+="Desarrollo Web"

    if movil.get(): # Sí me da True
        if web.get(): # Sí me da True
            texto+=" y Desarrollo Movil"
        else:
            texto+="Desarrollo Movil"


    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
    )

# Botones de Check
web= IntVar()
movil=IntVar()
Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0,sticky=W)
Checkbutton(
    ventana, 
    text="Desarrollo Web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0,sticky=W)
Checkbutton(
    ventana, 
    text="Desarrollo Movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0,sticky=W)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radio Buttons ( Solo se puede marcar una opcion)
def marcar():
    marcado.config(text=opcion.get())
opcion=StringVar()
opcion.set(None)

Label(ventana, text="¿Cual es tu genero?").grid(row=5, column=0,sticky=W)
Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6, column=0,sticky=W)
Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7, column=0,sticky=W)

marcado = Label(ventana)
marcado.grid(row=8)





# Option Menu
def seleccionar():
    seleccionado.config(text=opcion.get())
    

opcion=StringVar()

opcion.set("Opcion 1") # Por defecto

Label(ventana, text="Selecciona una opcion: ").grid(row=5, column=1,sticky=W)
select=OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=8, column=1)


seleccionado=Label(ventana)
seleccionado.grid(row=7, column=1)









ventana.mainloop()