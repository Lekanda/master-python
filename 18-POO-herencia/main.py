import clases   # Importa todas las clases del archivo 'clases.py'

persona=clases.Persona()
persona.setNombre('Andres')
persona.setApellidos('Bernaola Olibares')
persona.setAltura("190 cm")
persona.setEdad(" 45 años")

print(f"La persona es : {persona.getNombre()} {persona.getApellidos()}")
print(f"Edad : {persona.getEdad()} - Altura: {persona.getAltura()}")

print(persona.hablar())




