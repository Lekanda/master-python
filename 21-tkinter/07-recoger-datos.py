from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.title("Recoder datos de Formulario")
ventana.config(
    bd= 50
)

def getDato():
    resultado.set(dato.get())



dato = StringVar()
resultado=StringVar()

Label(ventana, text="Mete un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato Recogido: ").pack(anchor=NW)
texto_recogido=Label(ventana, textvariable=resultado)
texto_recogido.config(
    bg="green",
    fg="white"

)
texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar Dato", command=getDato).pack(anchor=NW)

ventana.mainloop()