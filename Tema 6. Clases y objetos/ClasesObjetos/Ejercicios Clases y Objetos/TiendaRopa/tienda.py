
class Tienda:

    def __init__(self):
        self.prendas = {}

    def agregar_prenda(self, codigo, prenda):
        self.prendas[codigo] = prenda
        print("Prenda añadida correctamente")

    def mostrar_prendas(self):

        if len(self.prendas) == 0:
            print("La tienda está vacía")

        else:
            for codigo, prenda in self.prendas.items():

                print("Código:", codigo)
                print("Nombre:", prenda.nombre)
                print("Precio original:", prenda.precio)
                print("Precio final:", round(prenda.calcular_precio_final(), 2))
                print("-------------------")

    def buscar_prenda(self, codigo):

        if codigo in self.prendas:
            prenda = self.prendas[codigo]

            print("Prenda:", prenda.nombre)
            print("Precio final:", round(prenda.calcular_precio_final(), 2))

        else:
            print("Prenda no encontrada")
