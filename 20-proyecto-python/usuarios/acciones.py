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
        print(f"Registro es : {registro}")
        print(registro[1])

        if registro[0] >=1:
            print(f"\nEl Usuario {registro[1].nombre} se ha registrado!!")
        else:
            print("\nNO te has registrado correctamente")

    def login(self):
        print("Vale; Identificate en el sistema!!")

        try:
            email =  input("¿Cual es tu email?: ")
            password = input("Introduce tu password: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]} te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            # print("type(e).__name__")
            print(f"Login incorrecto intentalo mas tarde")

    def proximasAcciones(self, usuario):
        return None
