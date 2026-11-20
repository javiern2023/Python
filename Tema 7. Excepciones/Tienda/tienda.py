class Tienda:

    def __init__(self):

        self.productos = {}

    def agregar_producto(self, codigo, producto):

        self.productos[codigo] = producto

        print("Producto añadido correctamente")

    def mostrar_productos(self):

        for codigo, producto in self.productos.items():

            print("\nCódigo:", codigo)

            producto.mostrar_informacion()

            print("-------------------")

    def vender_producto(self, codigo, cantidad):

        if codigo not in self.productos:

            print("El producto no existe")

        else:

            producto = self.productos[codigo]

            producto.vender(cantidad)