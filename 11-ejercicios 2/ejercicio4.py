"""
                Ejercicio 4
                -----------
- Crear un script con 4 variables, una lista , un string, un entero y un booleano y que imprima un mensaje segun el tipo de dato de cada variable.
-
"""

def comprobarTipado (dato,tipo) :
    test=isinstance(dato,tipo)
    result=""
    if test:
        result=f"Este dato es del tipo: {type(dato)}"
    else:
        result = None
    return result


num=10
boo=True
lista=["Hola","Juan","Pepe"]
string="Hola como estas"

tipoDatos = type(boo)
print(tipoDatos)
print(comprobarTipado(boo,tipoDatos))
