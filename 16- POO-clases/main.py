"""
        Programacion orientada a objetos(POO o OOP)
- SELF=> se pasa para pòder acceder a las propiedades de la clase        
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
    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1
    def getVelocidad(self):
        return self.velocidad
    
    #Fin de definicion de la CLASE


# Crear objetos/ Instanciar la clase
coche = Coche()

print(coche)
print(coche.marca)
print(coche.modelo)
print(coche.color)
print(coche.velocidad)
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
print(coche.getVelocidad())
coche.frenar()
coche.frenar()
print(coche.getVelocidad())
