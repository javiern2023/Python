
productos = [
    {"nombre": "Pan", "precio": 1.20},
    {"nombre": "Leche", "precio": 1.50},
    {"nombre": "Arroz", "precio": 2.00}
]

eliminar = input("¿Qué producto quieres eliminar? ")

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == eliminar.lower():
        productos.remove(producto)
        print("Producto eliminado correctamente.")
        encontrado = True
        break

if encontrado == False:
    print("El producto no existe.")

print("Lista final:", productos)
