import mysql.connector

def conectar():
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
    #--------------------------------------------
    #¿La conexion ha sido correcta?
    # print(database) 
    #--------------------------------------------
    cursor = database.cursor(buffered=True)
    # buffered=True => Nos permite hacer muchas consultas utilizando el mismo cursor
    # Cursor: Nos permite ejecutar las consultas
    #--------------------------------------------
    return [database, cursor]