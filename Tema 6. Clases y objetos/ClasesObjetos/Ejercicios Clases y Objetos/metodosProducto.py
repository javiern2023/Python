class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def modificar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def modificar_stock(self, nuevo_stock):
        self.stock = nuevo_stock

    def mostrar_producto(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Stock:", self.stock)


producto1 = Producto("Ratón", 20, 15)

producto1.mostrar_producto()

producto1.modificar_precio(25)
producto1.modificar_stock(30)

print("\nDespués de modificar:")

producto1.mostrar_producto()