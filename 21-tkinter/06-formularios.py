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
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=2, sticky=W)



#Label para el campo
label = Label(ventana, text="Nombre")
label.grid(row=1,column=0,padx=5,pady=5, sticky=W)
# Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5,pady=5)




ventana.mainloop()
