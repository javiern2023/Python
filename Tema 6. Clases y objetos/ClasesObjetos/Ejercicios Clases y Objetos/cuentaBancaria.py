class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        print("Dinero ingresado correctamente")

    def retirar_dinero(self, cantidad):
        self.saldo -= cantidad
        print("Dinero retirado correctamente")

    def mostrar_saldo(self):
        print("Titular:", self.titular)
        print("Saldo:", self.saldo, "euros")


cuenta1 = CuentaBancaria("Laura", 1000)

cuenta1.ingresar_dinero(200)
cuenta1.retirar_dinero(100)

cuenta1.mostrar_saldo()