
productos = [
    {"nombre": "Pan", "precio": 1.20},
    {"nombre": "Leche", "precio": 1.50},
    {"nombre": "Arroz", "precio": 2.00}
]

buscar = input("¿Qué producto quieres modificar? ")

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == buscar.lower():
        nuevo_precio = float(input("Introduce el nuevo precio: "))
        producto["precio"] = nuevo_precio
        print("Precio modificado correctamente.")
        encontrado = True
        break

if encontrado == False:
    print("El producto no existe.")

print("Lista actualizada:", productos)
