import clases   # Importa todas las clases del archivo 'clases.py'



print("-----------------------------------")
persona=clases.Persona()
persona.setNombre('Andres')
persona.setApellidos('Bernaola Olibares')
persona.setAltura("190 cm")
persona.setEdad(" 45 años")

print(f"La persona es : {persona.getNombre()} {persona.getApellidos()}")
print(f"Edad : {persona.getEdad()} - Altura: {persona.getAltura()}")

print(persona.hablar())

print("-----------------------------------")

informatico= clases.Informatico()
informatico.setNombre("Jon")
informatico.setApellidos("Paz Vega")
print(f"El Informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(f"El Informatico sabe estos lenguajes: {informatico.getLenguajes()}")
print(informatico.caminar())
print(informatico.experiencia)


print("-----------------------------------")
tecnico = clases.TecnicoRedes()
tecnico.setNombre("Luis")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.lenguajes)

"""
- Si no hay dato metido en el objeto , da error que no existe ese atributo/propiedad.
- Hay que meter el dato antes de leer el objeto
"""