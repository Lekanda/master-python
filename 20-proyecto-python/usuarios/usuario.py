import mysql.connector

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
        return self.nombre

    def indentificar(self):
        return self.nombre
