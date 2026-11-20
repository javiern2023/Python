
from abc import ABC, abstractmethod


class Libro(ABC):

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def mostrar_informacion(self):
        pass
