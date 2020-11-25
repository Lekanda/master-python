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

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

    # Comprobar que se ha creado la DB
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)