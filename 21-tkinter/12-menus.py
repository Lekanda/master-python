from tkinter import *

ventana=Tk()
ventana.geometry("600x600")


mi_menu=Menu(ventana)
ventana.config(menu=mi_menu)


archivo=Menu(mi_menu,tearoff=0) # tearoff => Quita la linea discontinua que sale en el menu
archivo.add_command(label="Nuevo Archivo")
archivo.add_command(label="Nueva Ventana")
archivo.add_separator()
archivo.add_command(label="Abrir Archivo")
archivo.add_command(label="Abrir Carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)# venta.quit => cierra la ventana


mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")






ventana.mainloop()