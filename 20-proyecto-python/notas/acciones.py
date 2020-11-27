import notas.nota as modelo

class Acciones :
    def crear(self,usuario):
        print(f"\nOk!! {usuario[1]} Vamos a crear una nueva nota..")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce una Nota")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Perfecto has guardado la Nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")
