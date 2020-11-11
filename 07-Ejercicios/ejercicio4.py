"""
CALCULADORA DE DOS NUMEROS PEDIDOS +-*/ resto
"""
num1=int(input("Dame un numero: "))
num2=int(input("Dame otro numero: "))

print("########## CALCULADORA ############")
ope=input("que operacion quieres hacer? +-*/ o resto")
resultado=0

if ope == "+":
    resultado=num1+num2
    print(f"La suma es: {resultado}")
elif ope == "-":
    resultado=num1-num2
    print(f"La resta es: {resultado}")
elif ope == "*":
    resultado=num1*num2
    print(f"La multiplicacion es: {resultado}")
elif ope == "/":
    resultado=num1/num2
    print(f"La division es: {resultado}")
elif ope == "resto":
    resultado=num1%num2
    print(f"El resto de la division es: {resultado}")
