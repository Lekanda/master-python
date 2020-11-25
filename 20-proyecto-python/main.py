"""
            APLICACION DE NOTAS EN CONSOLA
            ------------------------------
- abrir asistente que pregunte sí queremos hacer:
        - login
        - Registro
- Sí Registro = Crear Cuenta de Uss en la DB
- Sí login = Loguerse en la DB y menu de acciones desde la DB:
    - Crear Nota
    - Leer Nota
    - Borrar Nota
"""

# al  meter """  podemos poner varias lineas:
print("""
Acciones disponibles:
    - registro
    - login
""")
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    print("Ok!! Vamos a registrarte en el sitema...")
elif accion == "login":
    print("Vale; Identificate en el sistema!!")
