import mysql.connector
import datetime

##################
# Conexion a la DB
##################
database = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd = "nuvN52772of5VzNL",
    database = "master_python",
    port = 3306
)
#¿La conexion ha sido correcta?
# print(database) 

#--------------------------------------------
# Cursor: Nos permite ejecutar las consultas
cursor = database.cursor(buffered=True)
# buffered=True => Nos permite hacer muchas consultas utilizando el mismo cursor
#--------------------------------------------




class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s,%s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
        


    def indentificar(self):
        return self.nombre
