
from libro import Libro


class LibroDigital(Libro):

    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato

    def mostrar_informacion(self):
        print("LIBRO DIGITAL")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Formato:", self.formato)
