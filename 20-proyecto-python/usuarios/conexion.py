import mysql.connector

def conectar():
    ##################
    # Conexion a la DB
    ##################
    database = mysql.connector.connect(
        host ="localhost",
        user = "root",
        passwd = "xa6nXxyZkaHENeJ3",
        database = "master_python",
        port = 3308
    )
    #--------------------------------------------
    #¿La conexion ha sido correcta?
    # print(database) 
    #--------------------------------------------
    cursor = database.cursor(buffered=True)
    # buffered=True => Nos permite hacer muchas consultas utilizando el mismo cursor
    # Cursor: Nos permite ejecutar las consultas
    #--------------------------------------------
    return [database, cursor]