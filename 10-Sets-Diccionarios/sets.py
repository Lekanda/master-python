"""
***************** SETS *******************
------------------------------------------
- Set es un tipo de dato, para tener una coleccion de valores,
pero  no tiene ni indice ni orden
"""

personas = {
    "Andres",
    "Manolo",
    "Jon"
}

personas.add("Manuel")
personas.remove("Jon")



print(type(personas))
print(personas)