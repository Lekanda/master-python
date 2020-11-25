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
    print("\nOk!! Vamos a registrarte en el sitema...")
    nombre = input("¿Cual es tu nombre?: ")
    apellidos = input("¿Cuales son tus apellidos?: ")
    email =  input("¿Cual es tu email?: ")
    password = input("Introduce tu password: ")
elif accion == "login":
    print("Vale; Identificate en el sistema!!")
    email =  input("¿Cual es tu email?: ")
    password = input("Introduce tu password: ")