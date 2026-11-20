
from prenda import Prenda


class Camiseta(Prenda):

    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento

    def calcular_precio_final(self):
        return self.precio - (self.precio * self.descuento / 100)
