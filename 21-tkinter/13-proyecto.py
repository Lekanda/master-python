"""
                PROYECTO
                --------
- crear un programa que tenga:
    - Una ventana (X)
    - Tamaño fijo (X)
    - Ventana no redimensionable (X)
    - Un Menu superior (Inicio,Añadir, Informacion, Salir) (X)
    - Diferentes pantallas (X)
    - Formulario de añadir productos (X)
    - guardar datos temporalmente (X)
    - MOstrar datos listados en la pantalla 'home'   
    - Opcion de 'Salir' (X)       
"""
import tkinter as TK
# definir ventana
ventana=TK.Tk()
# ventana.geometry("500x500")
ventana.minsize("500x500") #Tamaño minimo de la ventana
ventana.title("Proyecto con TKINTER")
ventana.resizable(0,0)




# Pantallas
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=203,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=1)# Caja de productos en DB
    # Listar productos
    for product in products:
        if len(product)==3:
            product.append("added")
            TK.Label(products_box, text=product[0]).grid()
            TK.Label(products_box, text=product[1]).grid()
            TK.Label(products_box, text=product[2]).grid()
            TK.Label(products_box, text="----------------").grid()

    # Ocultar otras Pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True




def add():
    # Encabezado campos formulario
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0,columnspan=12)
    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1,column=0,padx=5,pady=5,sticky='E')
    add_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky='W')
    add_price_label.grid(row=2,column=0,padx=5,pady=5,sticky='E')
    add_price_entry.grid(row=2,column=1,padx=5,pady=5,sticky='W')
    add_description_label.grid(row=3,column=0,padx=5,pady=5,sticky='NE')
    add_description_entry.grid(row=3,column=1,padx=5,pady=5,sticky='W')
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas",12),
        padx=15,
        pady=15
    )
    add_separator.grid(row=4,column=1) # Separador
    boton.grid(row=5,column=1,sticky='NW')
    boton.config(
        padx=7,
        pady=5,
        # bg="black",
        # fg="white",
        activebackground="green"
    )
    # Ocultar otras Pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True




def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=145,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1,column=0)
    # Ocultar otras Pantallas
    add_label.grid_remove()
    products_box.grid_remove()
    add_frame.grid_remove()
    home_label.grid_remove()
    return True


def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0","end-1c")
    ])
    name_data.set("")# despues de guardar borra el nombre del producto en formulario
    price_data.set("")# despues de guardar borra el precio del producto en formulario
    add_description_entry.delete("1.0",TK.END)
    # print(products)

    home() # Manda a la pantalla de 'Home'

#Variables importantes
products = []
name_data = TK.StringVar()
price_data = TK.StringVar()


# Definir encabezado de Pantallas(INICIO/HOME)
home_label=TK.Label(ventana, text="Inicio")
products_box = TK.Frame(ventana, width=250, )

# Definir encabezado de Pantallas(ADD)
add_label=TK.Label(ventana, text="Añadir producto")
#Campos del formulario
add_frame= TK.Frame(ventana)
add_name_label = TK.Label(add_frame, text="Nombre del Producto: ")
add_name_entry = TK.Entry(add_frame, textvariable=name_data)
add_price_label = TK.Label(add_frame, text="Precio del Producto: ")
add_price_entry = TK.Entry(add_frame, textvariable=price_data)
add_description_label = TK.Label(add_frame, text="Descripción:")
add_description_entry = TK.Text(add_frame)
add_separator = TK.Label()
# Boton del Formulario
boton=TK.Button(add_frame, text="Guardar", command=add_product)




# Definir encabezado de Pantallas(INFO)
info_label=TK.Label(ventana, text="Informacion")
data_label=TK.Label(ventana, text="Creado por Andres Bernaola")


# Cargar la pantalla de inicio
home()


# Menu Superior
menu_superior=TK.Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)
# Cargar el menu superior
ventana.config(menu=menu_superior)


#Cargar ventana
ventana.mainloop()