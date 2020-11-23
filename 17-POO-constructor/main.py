"""
                        VISIBILIDAD
                        -----------
- Dentro de una clase podemos crear nuestros metodos y propiedades, pero estas deben ser o publicas o privadas, en funcion de la visibilidad que queramos que tenga en el resto del codigo.

    - PUBLICOS: Son por defecto

    - PRIVADAS: Son accesibles desde dentro de la clase. Es obligatorio usar getter para extraer los datos
        - Para declarar un atributo privado poner delante del nombre de archivo '__'. Ver en 'coche.py'

"""



# Importar la clase Coche
from coche import Coche 


carro=Coche("Verde","Audi","TT",250,240,2)
carro1=Coche("Amarillo","Ford","Galaxy",180,180,6)
carro2=Coche("Azul","KIA","Sorento",160,200,8)
carro3=Coche("Rojo","BMW","180TDI",260,300,4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())


# Detectar tipado
if type(carro3) == Coche:
    print("Es un objeto tipo COCHE")
else:
    print("No es un objeto tipo COCHE")


#Visibilidad. Explicacion arriba
    # Funciona por que es un propiedad publico
print(carro.soy_publico)
    # Falla por que es un propiedad privado
# print(carro.__soy_privado)
    # De esta forma accedemos a un metodo de una propiedad privada
print(carro.getPrivado())




