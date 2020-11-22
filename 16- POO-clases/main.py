"""
        Programacion orientada a objetos('POO' o 'OOP')
        -----------------------------------------------

- 'SELF'=> se pasa para pòder acceder a las propiedades de la clase  

- 'GETTER' para coger datos y 'SETTER' para asignar un valor nuevo o modificado

    *   print(coche.getVelocidad()) => Metodo 'GETTER'

    *   coche.acelerar() => Metodo 'SETTER'
    *   def setColor(self, color_nuevo): => Metodo 'SETTER'
            self.color=color_nuevo
    
"""

# Definir una clase COCHE
class Coche:

    # Propiedades
    color= "Rojo"
    marca="Ford"
    modelo="Scort"
    velocidad=300
    caballaje=500
    plazas=4

    # Metodos , son acciones que hace el objeto
        # Cambia color de coche
    def getColor(self):
        return self.color

        # Cambia color de coche
    def setColor(self, color):
        self.color=color

        # Cambia modelo de coche
    def setModelo(self, modelo):
        self.modelo=modelo

        # Cambia marca de coche
    def setMarca(self, marca):
        self.marca=marca

        # Coge el  modelo de coche
    def getModelo(self):
        return self.modelo
        
        # Sube 1 la velocidad
    def acelerar(self):
        self.velocidad+=1

        # Baja 1 la velocidad
    def frenar(self):
        self.velocidad-=1

        # Devuelve la velocidad actual
    def getVelocidad(self):
        return self.velocidad
    #Fin de definicion de la CLASE



# Crear objetos/ Instanciar la clase
print("************Coche 1**********")
coche = Coche()

print(coche)
print(coche.marca)
print(coche.modelo)
print(coche.color)

print(coche.velocidad)
coche.acelerar() # => SETTER
coche.acelerar()
coche.acelerar()
coche.acelerar()
print(coche.velocidad) # => GETTER
coche.frenar() # => SETTER
coche.frenar()
print(coche.getVelocidad())# => GETTER


coche.setColor("azul") # Cambiamos el color => SETTER
print(coche.color)



"""
- GETTER para coger datos y SETTER para asignar un valor nuevo o modificado
    *   print(coche.getVelocidad()) => Metodo GETTER
"""

print("***********Coche 2****************")
# CRear mas objetos
coche2=Coche()
coche2.setColor("Verde")
coche2.setModelo("Cobra")
coche2.setMarca("Audi")

print(coche2.marca,coche2.getModelo(),coche2.getColor())
print(type(coche2))

