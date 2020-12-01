"""
                    CALCULADORA
                    -----------
- dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta

"""
from tkinter import *
from tkinter import messagebox

ventana=Tk()
ventana.title("Ejercicio completo con Tkinter")
ventana.geometry("400x400")
ventana.config(
    bd=25
)

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error tipo Datos", "Introduce solo numeros")
        numero1.set("")
        numero2.set("")
def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error al meter numeros", "PorFavor; introduce solo numeros")
        numero1.set("")
        numero2.set("")
def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error al meter numeros", "PorFavor; introduce solo numeros")
        numero1.set("")
        numero2.set("")
def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error al meter numeros", "PorFavor; introduce solo numeros")
        numero1.set("")
        numero2.set("")

def mostrarResultado ():
    messagebox.showinfo("Resultado", f"El resultado es : {resultado.get()}")
    numero1.set("")
    numero2.set("")


numero1=StringVar()
numero2=StringVar()
resultado=StringVar()


marco = Frame(ventana, width=250, height=200)
marco.config(
    bd=5,
    padx=15,
    pady=15,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False) # Impide que cambie de tamaño



Label(marco, text="Numero 1: ").pack()
Entry(marco,  textvariable=numero1, justify=CENTER).pack()

Label(marco, text="Numero 2: ").pack()
Entry(marco,  textvariable=numero2, justify=CENTER).pack()

Label(ventana, text="").pack()

Button(marco, text="Suma", command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side=RIGHT, fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side=RIGHT, fill=X, expand=YES)
# fill=X, expand=YES => hace que se propaguen los 4 elementos y cogen su tamaño




ventana.mainloop()