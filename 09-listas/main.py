"""
                 **LISTAS (arrays)**
-Son colecciones de Datos/valores, bajo un unico nombre.
-Para acceder a esos valores usamos un indice numerico

- TUPLA: Es lo mismo que una lista pero sus valores no pueden cambiar. Para crearla con LIST ponerlo entre parentesis. Ver ejemplo abajo
"""

# Definir una lista
peliculas = ["Batman", "Spiderman", "el señor de los anillos", "terminator"]
  # Con tupla. Entre (). En 
cantantes = list(('Van Morrison', 'Yes', 'David Bowie', 'Neil Young'))
  # Linea 14 : Crea una lista desde el 2020 a 2050
years=list(range(2020,2050))
  # Se puede meter en un lista datos de diferentes tipos
variada= ["Andres", 30, 4.5, True, "texto"]

# print(peliculas)
# print(cantantes)
# print(years)
peliculas[1]="Gran Torino"

print(peliculas[0])
    # li-25.Empieza desde el final de la lista
print(peliculas[-2])
    # li-27 Saca del 1 al 3
print(cantantes[1:3])
    # li-29: Todos a partir del 0
print(cantantes[0:])

# Añadir elementos a una lista
cantantes.append("Lou Reed")
cantantes.append("Joan Baez")
print (cantantes)


