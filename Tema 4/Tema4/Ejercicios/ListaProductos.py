
productos = [
    {"nombre": "Pan", "precio": 1.20},
    {"nombre": "Leche", "precio": 1.50},
    {"nombre": "Arroz", "precio": 2.00},
    {"nombre": "Huevos", "precio": 3.00}
]

for producto in productos:
    print("Nombre:", producto["nombre"])
    print("Precio:", producto["precio"], "euros")
    print()
