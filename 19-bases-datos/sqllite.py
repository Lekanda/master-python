"""
sqlite: es una version ligera de SQL que trae incorporado Python
"""

# importar modulo 'sqlite3'***
import sqlite3

# Conexion a SQLite***
conexion=sqlite3.connect('./19-bases-datos/pruebas.db')

# Crear cursor. Es lo que permite hacer las consultas***
cursor=conexion.cursor()




#########################
# *** CREAR UNA TABLA ***
#########################
#Modo 1
# cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
#         "id INTEGER PRIMARY KEY AUTOINCREMENT,"+ # OBLIGATORIO ASI
#         "titulo VARCHAR(255), "+
#         "descripcion TEXT,"+
#         "precio int(255)"
# ")")
# Modo 2 (Mejor)
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo varchar(255),
        descripcion text,
        precio int(255)
);
""")

# Guardar Datos***
conexion.commit()





###################
# INSERTAR DATOS***
# #################
# Modo 1
# cursor.execute("INSERT INTO productos VALUES (null,'Super producto','Es un producto muy bueno',200 );")
# conexion.commit() # Guardar Datos
# Modo 2 (Mejor)
# cursor.execute("""INSERT INTO productos VALUES (null,
# 'Super producto',
# 'Es un producto muy bueno',
# 210 
# );""")
# conexion.commit() # Guardar Datos






#####################
#*** BORRAR DATOS ***
#####################
# cursor.execute("DELETE FROM productos") # CUIDADO: BORRA TODOS LOS DATOS





###########################################
#*** INSERTAR MUCHOS REGISTROS A LA VEZ ***
###########################################
productos = [
        ("Ordenador Portatil", "Buen PC", 700),
        ("Tablet", "Es una gran Tableta", 400),
        ("iPhone", "Movil de ultima generacion", 1700),
        ("Smart Watch", "Un gran Smart Watch", 100)
]
cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)", productos) # La var productos es el Array de objetos
conexion.commit()






#####################
#*** UPDATE DATOS ***
#####################
cursor.execute("UPDATE productos SET precio = 1900  WHERE precio = 1700")







##############################################
# *** LISTAR DATOS DE LA TABLA 'PRODUCTOS' ***
##############################################
cursor.execute("SELECT * FROM productos WHERE precio >= 1000;")
# print(cursor) # nos da un objeto pero de esta forma no se ven los datos
productos=cursor.fetchall() # Metemos en 'productos' los datos que se pueden ver
# print(productos) # Imprimir productos, ya visibles
for producto in productos: # Recorre los objetos de la DDBB
        print("ID:", producto[0])
        print(producto)
        print(producto[1]) # Coge solo el primer campo del registro
        print("Nombre Producto:",producto[1]) # Coge solo el primer campo del registro
        print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto=cursor.fetchone() # Nos da el titulo del primer producto de la DDBB
print(producto)


# cursor.execute("DELETE FROM productos")


############################
# *** CERRAR LA CONEXION ***
############################
conexion.close()

