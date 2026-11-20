from excepciones import StockInsuficienteError


class Producto:

    def __init__(self, nombre, precio, stock):

        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")

        if cantidad > self.stock:
            raise StockInsuficienteError("No hay suficiente stock")

        self.stock -= cantidad

        print("Venta realizada correctamente")

    def mostrar_informacion(self):

        print("Producto:", self.nombre)
        print("Precio:", self.precio, "euros")
        print("Stock disponible:", self.stock)
