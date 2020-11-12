"""
Funcion: Un conjunto de instrucciones agrupadas en un nombre

def nombreFuncion(parametros):
    # Bloque de codigo 


# Para invocar a la funcion
nombreFuncion(parametro/s)

"""



# Ejemplo 1
# nombre=input("dame un nombre: ")
# print("\n")
# print("########## EJEMPLO1 ##########")
# print("\n\n")

# def muestraNombres(nombre):
#     print("Andres")
#     print("Bernaola")
#     print(f"hola {nombre}")
#     print("\n\n")

# muestraNombres(nombre)









# Ejemplo 4 PARAMETROS OPCIONALES
"""
-Sí queremos que uuno de los argumentos de la funcion sea opcional:
 def empleado(nombre, dni=False o numero por defecto, None)

 -Se puede poner un if en el interior para que no lo haga

 if dni!=None:   lo hace

 -O pasar la 2ªvariable en el llamamiento de la funcion
"""


# Ejemplo 5 RETURN Y EJEMPLOS COMPLETOS
# num1=int(input("Dame un numero: "))
# num2=int(input("Dame otro numero: "))
# ope=input("Que operacion quieres hacer")
# resultado=0

# def calculadora(ope):
#     if ope == "+" :
#         resultado=num1+num2
#         return(resultado)
#     elif ope=="-":
#         resultado=num1-num2
#         return(resultado)
#     elif ope=="*":
#         resultado=num1*num2
#         return(resultado)
#     elif ope=="/":
#         resultado=num1/num2
#         return(resultado)
# print(f"El resultado es {calculadora(ope)}")

# En capitulo 42 ver ejemplo en min 4:00 aprox para crear cadenas







# Ejemplo 7 Funciones dentro de otras
# def getNombre(nombre):
#     texto = f"El nombre es : {nombre}"
#     return texto
# def getApellido(apellido):
#     texto = f"El apellido es : {apellido}"
#     return texto
# def devuelveTodo(nombre, apellido):
#     texto= getNombre(nombre) + " " + getApellido(apellido)
#     return texto

# # print(getNombre("andres"), getApellido("Bernaola"))

# print(devuelveTodo("Andres","Bernaola"))





"""
*Funciones LAMBDA: Son funciones anonimas para tareas simples y pequeñas pero pueden ser muy repetitivas, no tiene nombre
* Todo su contenido se traduce a una linea. No pueden ser complejas
"""

# Ejemplo 8 : FUNCIONES LAMBDA

# programa para decir en que año estamos

dime_el_year=lambda year: f"El año es : {year}"
print(dime_el_year(2020))