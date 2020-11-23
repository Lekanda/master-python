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
