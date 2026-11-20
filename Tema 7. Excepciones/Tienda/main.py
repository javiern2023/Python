from producto import Producto
from tienda import Tienda
from excepciones import StockInsuficienteError


tienda = Tienda()


producto1 = Producto("Portátil", 750, 10)

producto2 = Producto("Ratón", 20, 5)

producto3 = Producto("Teclado", 40, 8)


tienda.agregar_producto("P001", producto1)

tienda.agregar_producto("P002", producto2)

tienda.agregar_producto("P003", producto3)


print("\n=== PRODUCTOS DE LA TIENDA ===")

tienda.mostrar_productos()


print("\n=== REALIZAR VENTA ===")

try:

    codigo = input("Introduce el código del producto: ")

    cantidad = int(input("¿Cuántas unidades quieres comprar?: "))

    tienda.vender_producto(codigo, cantidad)

except StockInsuficienteError as error:

    print("Error:", error)

except ValueError as error:

    print("Error:", error)


print("\n=== STOCK ACTUALIZADO ===")

tienda.mostrar_productos()