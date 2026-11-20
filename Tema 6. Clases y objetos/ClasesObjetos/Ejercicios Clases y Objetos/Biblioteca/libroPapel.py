
from libro import Libro


class LibroPapel(Libro):

    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas

    def mostrar_informacion(self):
        print("LIBRO DE PAPEL")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Páginas:", self.paginas)
