import mysql.connector # Importar Connector para la conexion a la DB
##################
# Conexion a la DB
##################
database = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "nuvN52772of5VzNL",
    database = "master_python"
)
#¿La conexion ha sido correcta?
# print(database) 
# Bebe dar algo asi: <mysql.connector.connection.MySQLConnection object at 0x000001F89EE9E970>




#--------------------------------------------
# Cursor: Nos permite ejecutar las consultas
cursor = database.cursor(buffered=True)
    # buffered=True => Cuando se usa mucho el 'cursor' puede dar fallos. Para eso se pone esto
#---------------------------------------------





##########
# Crear DB
# ######## 
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
"""
# Comprobar que se ha creado la DB
cursor.execute("SHOW DATABASES")
# for db in cursor: # Itera en la  DB, las abiertas en MySQL
#     print(db)
"""





##############
# Crear Tablas
##############
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
# cursor.execute("SHOW TABLES")
# for table in cursor:
#     print(table) # Nos da las tablas creadas en la DB creada






################################################################
# Insertar datos en la DB 'vehiculos' y en la tabla 'vehiculo'
################################################################
"""
# cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Corsa',1000)") # Inserta un registro
coches = [
    ('Opel','Astra',1000),
    ('Opel','corsa',1500),
    ('Mercedes','s400',10000),
    ('BMW','s5000',20000),
    ('KIA','Sandero',8000)
]
cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)", coches) # Inserta muchos registros a la vez
database.commit() # Guarda en la DB
"""





###############################
# Leer/Listar datos desde la DB
###############################
# Modo 1
"""
cursor.execute("SELECT * FROM vehiculos")
# cursor.execute("SELECT marca, precio FROM vehiculos") # Trae esAs 2 propiedades solo
result = cursor.fetchall()

for coche in result:
    # print(coche)
    # print(coche[0])
    print(coche[1], coche[3])
"""

# Modo 2 ( Con mas condiciones de busqueda que el Modo 1)
"""
cursor.execute("SELECT * FROM vehiculos WHERE precio>9000 AND marca='BMW'")
# cursor.execute("SELECT marca, precio FROM vehiculos") # Trae esos 2 solo
result = cursor.fetchall()

for coche in result:
    # print(coche)
    # print(coche[0])
    print(coche[1], coche[3])
"""

# Modo 3 ( Con 'FetchOne' traemos solo el primer registro de la DB)
"""
cursor.execute("SELECT * FROM vehiculos")
# cursor.execute("SELECT marca, precio FROM vehiculos") # Trae esos 2 solo
coche = cursor.fetchone()
print(coche)
"""




####################
# Borrar un registro
####################
"""
# cursor.execute("DELETE FROM vehiculos") # Boora TODOS  los vehiculos CUIDADO
cursor.execute("DELETE FROM vehiculos WHERE marca='KIA'") # Borra el que tiene la marca 'KIA'
database.commit()
print(cursor.rowcount, "Borrados") # Nos da el mensaje cuando se ha borrado el registro
"""




#################################
# Actualizar un registro en la DB
#################################
cursor.execute("UPDATE vehiculos SET precio=900000 WHERE marca='Ferrari'")
database.commit()
print(cursor.rowcount, "Actualizados") # Nos da el mensaje cuando se ha actualizado el registro