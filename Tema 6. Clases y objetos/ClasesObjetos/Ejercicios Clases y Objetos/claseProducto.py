class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_producto(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio, "euros")
        print("Stock:", self.stock)


producto1 = Producto("Portátil", 750, 10)

producto1.mostrar_producto()