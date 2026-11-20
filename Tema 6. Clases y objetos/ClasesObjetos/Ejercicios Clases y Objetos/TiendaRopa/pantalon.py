
from prenda import Prenda


class Pantalon(Prenda):

    def __init__(self, nombre, precio, iva):
        super().__init__(nombre, precio)
        self.iva = iva

    def calcular_precio_final(self):
        return self.precio + (self.precio * self.iva / 100)
