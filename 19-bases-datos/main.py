import mysql.connector

# Conexion a la DB
database = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "nuvN52772of5VzNL",
    database = "master_python"
)

#¿La conexion ha sido correcta?
# print(database) 
# Bebe dar algo asi: <mysql.connector.connection.MySQLConnection object at 0x000001F89EE9E970>


# Cursor: Nos permite ejecutar las consultas
cursor = database.cursor()


# Crear DB 
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
"""
# Comprobar que se ha creado la DB
cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)
"""
# Crear Tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table) # Nos da las tablas creadas en la DB creada