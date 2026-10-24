
productos = [
    {"nombre": "Pan", "precio": 1.20},
    {"nombre": "Leche", "precio": 1.50},
    {"nombre": "Arroz", "precio": 2.00}
]

buscar = input("Introduce el nombre del producto: ")

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == buscar.lower():
        print("Producto encontrado:", producto["nombre"])
        print("Precio:", producto["precio"], "euros")
        encontrado = True

if encontrado == False:
    print("El producto no existe.")
