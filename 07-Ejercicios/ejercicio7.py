"""
Mostrar numeros impares ,entre dos numeros pedidos 
"""
num1=int(input("Dame un numero: "))
num2=int(input("Dame otro numero distinto: "))

if num1>num2:
    resultado=0
    for cont in range(num2,(num1+1)):
        # resultado=cont%2
        if (cont%2) != 0:
            print(f"{cont} es impar")
else:
    resultado=0
    for cont in range(num1,(num2+1)):
        # resultado=cont%2
        if (cont%2) != 0:
            print(f"{cont} es impar")