# -Capturar excepciones y manejar errores en codigo
#  susceptible a fallos y errores
"""
                TRY,EXCEPT,ELSE(op) Y FINALLY(op)
                ---------------------------------
- Esta es la forma que tiene python de hacer un try/catch de JavScript.
- El else y el finally son opcionales:
    -ELSE=> Lo hace si ha salido bien
    -FINALLY => Lo hace siempre. Haya ssalido bien o mal
- TRY Y EXCEPT => Como try(ok) catch(nok)
"""
try:
    nombre=input("Cual es tu nombre?: ")

    if len(nombre) >1:
        nombre_usuario ="El nombre es:  "+nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error mete bien el nombre")
else: # Opcional
    print("Todo ha ido bien!!")
finally:
    print("Fin de la iteracion")
