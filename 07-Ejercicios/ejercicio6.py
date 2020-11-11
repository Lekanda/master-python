"""
mostrar todas las tablas de multiplicar del 1 al 10
"""
cont=1
resultado=0

while cont<=10:
    print(f"TABLA DEL {cont}")
    for num in range(1,11):
        resultado=cont*num
        print(f"Tabla del {cont}: {cont} x {num} igual a {resultado}")
    print(f"Tabla del {cont} finalizada")
    print("\n\n")
    cont+=1
