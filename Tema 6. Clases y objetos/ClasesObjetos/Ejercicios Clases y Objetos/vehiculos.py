class Vehiculo:

    def __init__(self, marca):
        self.marca = marca

    def mostrar_informacion(self):
        print("Marca:", self.marca)

    def arrancar(self):
        print("El vehículo está arrancando")


class Coche(Vehiculo):

    def arrancar(self):
        print("El coche está arrancando")


class Moto(Vehiculo):

    def arrancar(self):
        print("La moto está arrancando")


coche1 = Coche("Toyota")
moto1 = Moto("Yamaha")

coche1.mostrar_informacion()
coche1.arrancar()

moto1.mostrar_informacion()
moto1.arrancar()