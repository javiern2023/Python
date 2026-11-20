
class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro añadido correctamente")

    def mostrar_libros(self):

        if len(self.libros) == 0:
            print("La biblioteca está vacía")

        else:
            for libro in self.libros:
                libro.mostrar_informacion()
                print("-------------------")
