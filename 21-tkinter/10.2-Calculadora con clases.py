from tkinter import *
from tkinter import messagebox as Mensajes
from calculadora import Calculadora 
 
ventana = Tk()
ventana.title("Calculadora con class")
ventana.geometry("135x200")
#********* Clase calculadora ***********
calc = Calculadora()
#********* Variables ***********
tmp_numero1 = StringVar()
#********* Funcion que se llama cada vez que se presiona un boton ***********
def agregarNumeroOperacion(oper):
    calc.agregar(tmp_numero1.get())
    tmp_numero1.set("")#vacio el display
    if oper=="igual":
        resultado = calc.calcular()
        tmp_numero1.set(resultado)#muestro el resultado
    else:
        calc.agregar(oper)
 
#****** MARCO1 para display ***********************
marco1 = Frame(ventana, width=100, height=100)
marco1.config(bg="red", bd=5, relief="raise")
marco1.grid(row=0 , column=5, columnspan=12)
#***********************************
display = Entry(marco1, textvariable=tmp_numero1, width=20)
display.grid(row=0 , column=0)
 
#******* Marco2 para botones ************************
marco2 = Frame(ventana, width=300, height=300)
marco2.config(bg="green", bd=5, relief="raise")
marco2.grid(row=1 , column=5)
 
#***** Teclas ******************
#****** Botones 7 8 9 / ************
#***********************************
boton_7 = Button(marco2, text="7", command=lambda :tmp_numero1.set(tmp_numero1.get()+"7"), width=3, height=2)
boton_7.grid(row=0 , column=0)
#***********************************
boton_8 = Button(marco2, text="8", command=lambda :tmp_numero1.set(tmp_numero1.get()+"8"), width=3, height=2)
boton_8.grid(row=0 , column=1)
#***********************************
boton_9 = Button(marco2, text="9", command=lambda :tmp_numero1.set(tmp_numero1.get()+"9"), width=3, height=2)
boton_9.grid(row=0 , column=2)
#***********************************
boton_div = Button(marco2, text="/", command=lambda : agregarNumeroOperacion("dividir"), width=3, height=2)
boton_div.grid(row=0 , column=3)
 
#***********************************
#****** Botones 4 5 6 * *************
#***********************************
boton_4 = Button(marco2, text="4", command=lambda :tmp_numero1.set(tmp_numero1.get()+"4"), width=3, height=2)
boton_4.grid(row=1 , column=0)
#***********************************
boton_5 = Button(marco2, text="5", command=lambda :tmp_numero1.set(tmp_numero1.get()+"5"), width=3, height=2)
boton_5.grid(row=1 , column=1)
#***********************************
boton_6 = Button(marco2, text="6", command=lambda :tmp_numero1.set(tmp_numero1.get()+"6"), width=3, height=2)
boton_6.grid(row=1 , column=2)
#***********************************
boton_mult = Button(marco2, text="*", command=lambda :agregarNumeroOperacion("multiplicar"), width=3, height=2)
boton_mult.grid(row=1 , column=3)
 
#***********************************
#****** Botones 1 2 3 + *************
#***********************************
boton_1 = Button(marco2, text="1", command=lambda :tmp_numero1.set(tmp_numero1.get()+"1"), width=3, height=2)
boton_1.grid(row=2 , column=0)
#***********************************
boton_2 = Button(marco2, text="2", command=lambda :tmp_numero1.set(tmp_numero1.get()+"2"), width=3, height=2)
boton_2.grid(row=2 , column=1)
#***********************************
boton_3 = Button(marco2, text="3", command=lambda :tmp_numero1.set(tmp_numero1.get()+"3"), width=3, height=2)
boton_3.grid(row=2 , column=2)
#***********************************
boton_sum = Button(marco2, text="+", command=lambda : agregarNumeroOperacion("sumar"), width=3, height=2)
boton_sum.grid(row=2 , column=3)
 
#***********************************
#****** Botones 0 CA = - ***********
#***********************************
boton_0 = Button(marco2, text="0", command=lambda :tmp_numero1.set(tmp_numero1.get()+"0"), width=3, height=2)
boton_0.grid(row=3 , column=0)
#***********************************
boton_CA = Button(marco2, text="CA", command=lambda :tmp_numero1.set(""), width=3, height=2)
boton_CA.grid(row=3 , column=1)
#***********************************
boton_igual = Button(marco2, text="=", command=lambda :agregarNumeroOperacion("igual"), width=3, height=2)
boton_igual.grid(row=3 , column=2)
#***********************************
boton_res = Button(marco2, text="-", command=lambda : agregarNumeroOperacion("restar"), width=3, height=2)
boton_res.grid(row=3 , column=3)
 
ventana.mainloop()