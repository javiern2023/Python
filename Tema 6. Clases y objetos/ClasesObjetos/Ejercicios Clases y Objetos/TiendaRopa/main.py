
from camiseta import Camiseta
from pantalon import Pantalon
from tienda import Tienda


tienda = Tienda()


camiseta1 = Camiseta("Camiseta básica", 20, 10)
pantalon1 = Pantalon("Pantalón vaquero", 40, 21)

camiseta2 = Camiseta("Camiseta deportiva", 30, 15)
pantalon2 = Pantalon("Pantalón corto", 25, 21)


tienda.agregar_prenda("C001", camiseta1)
tienda.agregar_prenda("P001", pantalon1)
tienda.agregar_prenda("C002", camiseta2)
tienda.agregar_prenda("P002", pantalon2)


print("\n=== CATÁLOGO DE LA TIENDA ===")

tienda.mostrar_prendas()


print("\n=== BUSCAR PRENDA ===")

tienda.buscar_prenda("C001")
