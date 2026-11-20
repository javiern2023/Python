
from libro_papel import LibroPapel
from libro_digital import LibroDigital
from biblioteca import Biblioteca


biblioteca = Biblioteca()

libro1 = LibroPapel("Don Quijote", "Cervantes", 500)
libro2 = LibroDigital("El Principito", "Saint-Exupéry", "PDF")
libro3 = LibroPapel("La Celestina", "Fernando de Rojas", 300)
libro4 = LibroDigital("1984", "George Orwell", "EPUB")


biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)


print("\n=== BIBLIOTECA ===")

biblioteca.mostrar_libros()
