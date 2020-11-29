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
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)


#********** CAMPO NOMBRE ****************
#Label para el campo
label = Label(ventana, text="Nombre")
label.grid(row=1,column=0,sticky=W, padx=5,pady=5)
# Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5,pady=5)
campo_texto.config(justify="right", state="normal")

#********** CAMPO APELLIDOS ****************
#Label para el campo
label = Label(ventana, text="Apellidos")
label.grid(row=2,column=0, sticky=W, padx=5,pady=5)
# Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5,pady=5)
campo_texto.config(justify="right", state="normal")

#********** CAMPO TXT GRANDE ****************
#Label para el descripcion
label = Label(ventana, text="Descrpción")
label.grid(row=3,column=0, sticky=NW, padx=5,pady=5)
# Campo txt grande
campo_grande = Text(ventana)
campo_grande.grid(row=3,column=1,sticky=W)
campo_grande.config(
    width=30, 
    height=5, 
    state="normal",
    font=("Arial", 12),
    padx=5,
    pady=5
)


ventana.mainloop()
