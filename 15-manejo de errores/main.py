# -Capturar excepciones y manejar errores en codigo
#  susceptible a fallos y errores
"""
                TRY,EXCEPT,ELSE(op) Y FINALLY(op)
                ---------------------------------
- Seria en  python como hacer un try/catch similar al de JavScript.
- El else y el finally son opcionales:
    -ELSE=> Lo hace si ha salido bien
    -FINALLY => Lo hace siempre. Haya salido bien o mal
- TRY Y EXCEPT => Como 'try(ok) / catch(nok)'
"""



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
"""




# MULTIPLES excepciones
"""
try:
    numero=int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado del numero es: " + str(numero*numero))

# Error de codigo    
except TypeError:
    print("Debes convertir tus cadenas a entero en el codigo")

# Error de letras y vacio
# except ValueError:
#     print("Ni vacio ni letras, introduce un numero")

# error personalizado. No va si typeError esta puesto
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)
"""





# Excepciones Personalizadas o lanzar excepcion
try:
    
    nombre = input("Introduce el nombre:  ")
    edad = int(input("introduce la edad : "))

    if edad<5 or edad>110:
        raise ValueError("La edad no es real")
    elif len(nombre)<=1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al Master en Python {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error: ", e)

