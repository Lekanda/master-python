"""

# FOR
for var in elementoIterable
    instrucciones

"""

# Ejercicio 1
# contador=0
# resultado=0

# for contador in range(0,5):
#     print(f"Voy por el {contador}")
#     print(f"Voy por el " + str(contador))

#     resultado+=contador
#     print(f"{resultado}")

# Ejercicio 2
numero = int(input("Dame un numero:  "))
resultado=0

if numero>=1:
    print(f"Tabla del {numero}")
    for contador in range(1,11):
        resultado=numero*contador
        print(f"{numero} x {contador} igual {resultado} ")
        resultado=0
else:
    print("Un numero mayor que 1")

print("Tabla lista")