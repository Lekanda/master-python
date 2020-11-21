"""
                    Ejercicio 3
                    -----------
- Programa que comprueba sí una var esta vacia ,y si esta vacia llenarla con texto en minusculas y mostrarlo en mayuculas                    
"""

texto="Hola amigo"

if len(texto.strip()) <= 0:
    texto="hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")
# print(texto)
