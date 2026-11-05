productos = {
    "pan": 1.00,
    "leche": 1.20,
    "huevos": 2.50,
    "arroz": 1.80,
    "aceite": 3.50
}

carrito = {}

def mostrar_productos():
    print("\n--- PRODUCTOS ---")
    for producto, precio in productos.items():
        print(producto, "-", precio, "€")

def agregar_carrito(producto, cantidad):
    if producto in productos:
        if producto in carrito:
            carrito[producto] += cantidad
        else:
            carrito[producto] = cantidad
        print("Producto añadido al carrito")
    else:
        print("Producto no encontrado")

def mostrar_carrito():
    print("\n--- CARRITO ---")

    if len(carrito) == 0:
        print("El carrito está vacío")
    else:
        for producto, cantidad in carrito.items():
            precio = productos[producto] * cantidad
            print(producto, "x", cantidad, "=", precio, "€")

def calcular_total():
    total = 0

    for producto, cantidad in carrito.items():
        total += productos[producto] * cantidad

    return total

def finalizar_compra():
    total = calcular_total()
    print("\nTotal de la compra:", total, "€")
    print("Gracias por comprar en nuestra tienda")

def menu():
    while True:
        print("\n--- MINI TIENDA ---")
        print("1. Mostrar productos")
        print("2. Añadir al carrito")
        print("3. Mostrar carrito")
        print("4. Calcular total")
        print("5. Finalizar compra")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_productos()

        elif opcion == "2":
            producto = input("Nombre del producto: ").lower()
            cantidad = int(input("Cantidad: "))
            agregar_carrito(producto, cantidad)

        elif opcion == "3":
            mostrar_carrito()

        elif opcion == "4":
            print("Total:", calcular_total(), "€")

        elif opcion == "5":
            finalizar_compra()
            break

        elif opcion == "6":
            print("Saliendo de la tienda...")
            break

        else:
            print("Opción no válida")

menu()