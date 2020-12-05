### Entrada / Salida
```python
# entrada datos
nombre = input("Cual es tu nombre?: ")
edad = input("Cual es tu edad?: ")
#salida de datos
print(f"Tu nombre es {nombre} y tienes {edad} años")
# Al meter la edad es un str y hay que cambiarla a int para operar con ella
print(f"Tu nombre es {nombre} y tienes {int(edad)+2} años")
```