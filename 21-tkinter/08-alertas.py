from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title("Alertas en Tkinter")
# ventana.geometry("700x400")
ventana.config(
    bd=70
)


def sacarAlerta():
   MessageBox.showinfo("Alerta", "Hola soy el mss de alerta")

Button(ventana, text="Mostrar Alertas!!", command=sacarAlerta).pack()

def salir():
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando la aplicacion")
    if resultado != "yes" :
        ventana.destroy()

Button(ventana, text="¿Salir?", command=salir).pack()

ventana.mainloop()