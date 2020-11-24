"""
sqlite: es una version ligera de SQL que trae incorporado Python
"""

# importar modulo 'sqlite3'
import sqlite3

# Conexion a SQLite
conexion=sqlite3.connect("prueba.db")

# Crear cursor. Es lo que permite hacer las consultas
cursor=conexion.cursor()

# Crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"+ # OBLIGATORIO ASI
        "titulo VARCHAR(255), "+
        "descripcion TEXT,"+
        "precio int(255)"
")")

# Cerrar la conexion
conexion.commit()

# Cerrar la conexion
conexion.close()

# Crear una tabla
