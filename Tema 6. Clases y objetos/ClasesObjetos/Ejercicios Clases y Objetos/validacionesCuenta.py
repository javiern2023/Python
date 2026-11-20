class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("Ingreso realizado")
        else:
            print("Cantidad no válida")

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            print("Cantidad no válida")

        elif cantidad > self.saldo:
            print("No tienes suficiente saldo")

        else:
            self.saldo -= cantidad
            print("Retirada realizada")

    def mostrar_saldo(self):
        print("Saldo actual:", self.saldo, "euros")


cuenta1 = CuentaBancaria("Laura", 500)

cuenta1.ingresar_dinero(100)
cuenta1.retirar_dinero(200)
cuenta1.retirar_dinero(1000)

cuenta1.mostrar_saldo()