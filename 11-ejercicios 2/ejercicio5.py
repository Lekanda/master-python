"""
                    Ejercicio 5
                    -----------
- Crear una lista con el contenido de una tabla:
- Mostrar esta informacion ordenada
"""

diccionario = []

tabla = [
    {
    "categoria": "Accion",
    "juegos": ['gta','COD','PUG']
    },
    {
    "categoria": "aventura",
    "juegos": ['assins','crash','prince']
    },
    {
    "categoria": "deportes",
    "juegos": ['Fifa2021','Pro 21','Gp21']
    }
]

for categoria in tabla :
    print(f"--------{categoria['categoria']}")

    for juego in categoria['juegos']:
        cont=0
        print(juego)
        cont=+1
