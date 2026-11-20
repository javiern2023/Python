
from abc import ABC, abstractmethod


class Prenda(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self):
        pass
