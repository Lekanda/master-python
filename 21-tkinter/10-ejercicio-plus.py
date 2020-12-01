"""
                    CALCULADORA
                    -----------
- dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta

"""
from tkinter import *
from tkinter import messagebox


class Calculadora:
    

    def __init__(self,alertas):
        self.numero1=StringVar()
        self.numero2=StringVar()
        self.resultado=StringVar()
        self.alertas=alertas


    def cFloat (self,numero):
        try:
            result=float(numero)
            return result
        except :
            result = 0
            # messagebox.showerror("Error convirtiendo Datos","Introduce solo numeros por favor")
            # return result
    def sumar(self):
        try:
            self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get()))
            self.mostrarResultado()
        except:
            messagebox.showerror("Error tipo Datos", "Introduce solo numeros +")
            self.numero1.set("")
            self.numero2.set("")
    def restar(self):
        try:
            self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get()))
            self.mostrarResultado()
        except:
            messagebox.showerror("Error al meter numeros", "PorFavor; introduce solo numeros")
            self.numero1.set("")
            self.numero2.set("")
    def multiplicar(self):
        try:
            self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get()))
            self.mostrarResultado()
        except:
            messagebox.showerror("Error al meter numeros", "PorFavor; introduce solo numeros")
            self.numero1.set("")
            self.numero2.set("")
    def dividir(self):
        try:
            self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get()))
            self.mostrarResultado()
        except:
            messagebox.showerror("Error al meter numeros", "PorFavor; introduce solo numeros")
            self.numero1.set("")
            self.numero2.set("")

    def mostrarResultado (self):
        self.alertas.showinfo("Resultado", f"El resultado es : {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")



ventana=Tk()
ventana.title("Ejercicio completo con Tkinter")
ventana.geometry("400x400")
ventana.config(
    bd=25
)


calculadora=Calculadora(messagebox)


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
Entry(marco,  textvariable=calculadora.numero1, justify=CENTER).pack()

Label(marco, text="Numero 2: ").pack()
Entry(marco,  textvariable=calculadora.numero2, justify=CENTER).pack()

Label(ventana, text="").pack()

Button(marco, text="Suma", command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side=RIGHT, fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side=RIGHT, fill=X, expand=YES)
# fill=X, expand=YES => hace que se propaguen los 4 elementos y cogen su tamaño



ventana.mainloop()