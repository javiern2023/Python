class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def arrancar(self):
        self.encendido = True
        print("El coche ha arrancado")

    def detener(self):
        self.encendido = False
        print("El coche se ha detenido")


coche1 = Coche("Toyota", "Corolla")

coche1.arrancar()
coche1.detener()