import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sitema...")
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email =  input("¿Cual es tu email?: ")
        password = input("Introduce tu password: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >=1:
            print(f"El Usuario {registro[1].nombre} se ha registrado!!")
        else:
            print("NO te has registrado correctamente")

    def login(self):
        print("Vale; Identificate en el sistema!!")
        email =  input("¿Cual es tu email?: ")
        password = input("Introduce tu password: ")