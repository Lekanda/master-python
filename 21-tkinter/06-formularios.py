from tkinter import *

ventana= Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter")



# Texto encabezado
encabezado=Label(ventana, text="Formularios con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Cambria",18),
    padx=7,
    pady=7
)
encabezado.pack(side=LEFT,anchor=NW, fill=X, expand=YES)






ventana.mainloop()
