class Coche:

    # ***Propiedades***
    color= "Rojo"
    marca="Ford"
    modelo="Scort"
    velocidad=300
    caballaje=500
    plazas=4

    # *** Constructor***
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas






    # ***Metodos , son acciones que hace el objeto***
        # Obtiene color de coche
    def getColor(self):
        return self.color

        # Cambia color de coche
    def setColor(self, color):
        self.color=color



        # Cambia modelo de coche
    def setModelo(self, modelo):
        self.modelo=modelo

        # Coge el  modelo de coche
    def getModelo(self):
        return self.modelo
        


        # Cambia marca de coche
    def setMarca(self, marca):
        self.marca=marca

         # Obtiene marca de coche
    def getMarca(self):
        return self.marca



        # Sube 1 la velocidad
    def acelerar(self):
        self.velocidad+=1

        # Baja 1 la velocidad
    def frenar(self):
        self.velocidad-=1

        # Devuelve la velocidad actual
    def getVelocidad(self):
        return self.velocidad


        # Metodo general que llama a todos
    def getInfo(self):

        info = "------Informacion del coche-------------"
        info += "\n Color: "+self.getColor()
        info += "\n Marca: "+self.getMarca()
        info += "\n Modelo: "+self.getModelo()
        info += "\n Velocidad: "+str(self.getVelocidad())

        return info
    #Fin de definicion de la CLASE