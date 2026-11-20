class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_usuario(self):
        print("Usuario:", self.nombre)


libro1 = Libro("Don Quijote", "Miguel de Cervantes")

usuario1 = Usuario("Carlos")

usuario1.mostrar_usuario()

print("Libro:", libro1.titulo)
print("Autor:", libro1.autor)