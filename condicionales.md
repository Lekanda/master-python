### Condicionales


---


> Los operadores son **+ - * /**

>> Se utiliza **and**, **or**, **>=**, **<=**, **==**


```python
# Ejemplo 1********************
print("############EJEMPLO1#################")
color="rojo"
color2=input("Dame un color?: ")

if color2 == "rojo":
    print("el color es rojo")
else:
    print("el color no es rojo")


# Ejemplo 2****************************
"""
# Operadores de comparacion
== igual
!= distinto
< menor que 
> mayor que
<= menor o igual
>= mayor o igual
"""
print("############EJEMPLO2#################")

year=2020
year=input("Que año?: ")

if int(year) >= 2021:
    print("Estamos en 2021 para adelante")
else:
    print("Estamos antes de 2021")



year=int(input("Que año?: "))

if year >= 2021:
    print("Estamos en 2021 para adelante")
else:
    print("Estamos antes de 2021")



print("############EJEMPLO3#################")

nombre="Andres"
ciudad="Barcelona"
continente="Europa"
edad=15
mayoria_edad=18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "Europa":
        print("No es de Europa")
    else:
        print(f"Es de Europa y de la ciudad de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")

    if continente != "Europa":
        print("No es de Europa")
    else:
        print(f"Es de Europa y de la ciudad de {ciudad}")



print("############EJEMPLO4#################")

dia = int(input("introduce el dia de la semana; Numero 1-7: "))

if dia == 1:
    print("Es lunes")
elif dia==2:
    print("Es Martes")
elif dia==3:
    print("Es Miercoles")
elif dia==4:
    print("Es Jueves")
elif dia==5:
    print("Es Viernes")
elif dia==6:
    print("Es Sabado")
else:
    print("Es Domingo")


print("############EJEMPLO5#################")

edad_minima= 18
edad_maxima= 65
edad_real=int(input("Cual es tu Edad??: "))
sexo=input("Cual es tu sexo?? m/f: ")


if edad_real >= edad_minima and edad_real <= edad_maxima or sexo=="m":
    print("Estas en Edad de trabajar, mas si eres hombre")
else:
    print("No estas en edad de trabajar")



print("############EJEMPLO6#################")
edad_minima= 18
edad_maxima= 65
edad_real=int(input("Cual es tu Edad??: "))
sexo=input("Cual es tu sexo?? m/f: ")

if not(edad_real >= edad_minima and edad_real <= edad_maxima or sexo=="m"):
    print(" No Estas en Edad de trabajar")
else:
    print("A trabajar, mas si eres hombre")
```