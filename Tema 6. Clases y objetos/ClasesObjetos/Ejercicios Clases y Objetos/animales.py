class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido")


class Perro(Animal):

    def hacer_sonido(self):
        print(self.nombre, "dice: Guau")


class Gato(Animal):

    def hacer_sonido(self):
        print(self.nombre, "dice: Miau")


perro1 = Perro("Toby")
gato1 = Gato("Michi")

perro1.hacer_sonido()
gato1.hacer_sonido()