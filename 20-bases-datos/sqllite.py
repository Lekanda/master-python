"""
sqlite: es una version ligera de SQL que trae incorporado Python
"""

# importar modulo 'sqlite3'***
import sqlite3

# Conexion a SQLite***
conexion=sqlite3.connect("prueba.db")

# Crear cursor. Es lo que permite hacer las consultas***
cursor=conexion.cursor()

# Crear una tabla***
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"+ # OBLIGATORIO ASI
        "titulo VARCHAR(255), "+
        "descripcion TEXT,"+
        "precio int(255)"
")")
# Guardar Datos***
conexion.commit()

# INSERTAR DATOS***
cursor.execute("INSERT INTO productos VALUES (null,'Super producto','Es un producto muy bueno',200 );")
conexion.commit() # Guardar Datos

# LEER LOS DATOS DE LA TABLA 'PRODUCTOS'***
cursor.execute("SELECT * FROM productos;")
# print(cursor) # nos da un objeto pero de esta forma no se ven los datos
productos=cursor.fetchall() # Metemos en 'productos' los datos que ya son visibles
# print(productos) # Imprimir productos, ya visibles
for producto in productos: # Recorre los objetos de la DDBB
        print(producto)
        print(producto[1]) # Coge solo el primer campo del registro
        print("Nombre Producto:",producto[1]) # Coge solo el primer campo del registro
        print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto=cursor.fetchone() # Nos da el primer producto de la DDBB
print(producto)



# CERRAR LA CONEXION***
conexion.close()

