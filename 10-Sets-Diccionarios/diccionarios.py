"""
***************** Diccionarios *******************
--------------------------------------------------
- Es un tipo de dato que almacena un conjunto de datos en formato clave-valor y es parecido a un array asociativo o un objeto JSON. Son como las listas pero en vez de tener indice numerico, lo tiene alfanumerico

"""

persona = {
    "nombre": " Andres",
    "apellidos": "Bernaola",
    "web": "www.andresbernaola.com"
}

print(persona)
print(type(persona))
print(persona["apellidos"])
print(persona["web"])
print("\n\n")



# Lista con Diccionarios(En JS Array de Objetos JSON)
contactos = [
    {
        'nombre': 'Andres',
        'email': 'andres@andres.com'
    },
    {
        'nombre': 'Jon',
        'email': 'jon@andres.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    }
]


print(contactos)
print(contactos[0]['nombre'])
print(contactos[0]['email'])
contactos[0]['nombre'] = "Andresito"
print(contactos[0]['nombre'])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre: {contacto['nombre']}")
    print(f"email: {contacto['email']}")





