"""
# WHILE
Estructura de control que itera o repite una instruccion/es tantas veces como sea necesario hasta que deje de cumplirse la condicion.

while condicion:
    instrucciones
    actualizar el contador

"""

#   Ejercicio imprimir del 1 al 100 con While
# numero=1

# while numero<=100:
#     print(f"{numero}")
#     numero+=1
# print("Bucle acabado")

# numero=1
# muestrame = str(0)

# while numero<=100:
#     muestrame= muestrame + "," + str(numero)
#     numero+=1
# print(f"{muestrame}")
# print("Bucle acabado")




# Tabla de multiplicar con while


numero = int(input("Dame un numero:  "))
cont=1
resultado=0

if numero>=1:
    print(f"Tabla del {numero}")
    while cont <=10:
        resultado=numero*cont
        print(f"{numero} x {cont} igual a {resultado}")
        resultado=0
        cont+=1
else:
    print("Un numero mayor o igual a 1")
    
print("Tabla lista")

