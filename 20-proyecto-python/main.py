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
from usuarios import acciones

# al  meter """  podemos poner varias lineas:
print("""
Acciones disponibles:
    - registro
    - login
""")

hazEl = acciones.Acciones() # Instanciar la clase Acciones

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()