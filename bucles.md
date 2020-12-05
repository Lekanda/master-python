### Bucles


---


##### Bucle FOR
```python
"""
# FOR
for var in elementoIterable
    instrucciones
"""

# Ejercicio 1
contador=0
resultado=0
for contador in range(0,5):
    print(f"Voy por el {contador}")
    print(f"Voy por el " + str(contador))
    resultado+=contador
    print(f"{resultado}")

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
```


---


##### Bucle WHILE

```python
"""
#                       WHILE
- Estructura de control que itera o repite una instruccion/es tantas veces como sea necesario hasta que deje de cumplirse la condicion.
                while condicion:
                    instrucciones
                    actualizar el contador
"""
#   Ejercicio imprimir del 1 al 100 con While
numero=1
while numero<=100:
    print(f"{numero}")
    numero+=1
print("Bucle acabado")
numero=1
muestrame = str(0)
while numero<=100:
    muestrame= muestrame + "," + str(numero)
    numero+=1
print(f"{muestrame}")
print("Bucle acabado")
 

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
```