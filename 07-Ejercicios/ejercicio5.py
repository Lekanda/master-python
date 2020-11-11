"""
MOSTRAR TODOS LOS NUMEROS ENTRE DOS NUMEROS PEDIDOS
"""
num1=int(input("Dame un numero: "))
num2=int(input("Dame otro numero: "))

if num1>num2:
    while num2<=num1:
        print(num2)
        num2+=1
else:
    while num1<=num2:
        print(num1)
        num1+=1