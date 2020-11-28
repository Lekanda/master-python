import notas.nota as modelo

class Acciones :
    def crear(self,usuario):
        print(f"\nOk!! {usuario[1]} Vamos a crear una nueva nota..")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce una Nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la Nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self,usuario):
        print(f"\nVale {usuario[1]} estas son tus notas:")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n*********************************")
            print(f"Nota: {nota[0]}")
            print(nota[2])
            print(nota[3])
            print("\n")
            print("\n*********************************")


    def borrar(self, usuario):
        print(f"\nOK; {usuario[1]}!! Vamos a borrar Notas:  ")

        titulo=input("Que nota quieres borrar. Por Titulo: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota, prueba luego....")

