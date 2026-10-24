
productos = [
    {"nombre": "Pan", "precio": 1.20},
    {"nombre": "Leche", "precio": 1.50},
    {"nombre": "Arroz", "precio": 2.00}
]

opcion = 0

while opcion != 6:
    print("\n--- MINI TIENDA ---")
    print("1. Mostrar productos")
    print("2. Añadir producto")
    print("3. Buscar producto")
    print("4. Modificar precio")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        if len(productos) == 0:
            print("No hay productos.")
        else:
            for producto in productos:
                print(producto["nombre"], "-", producto["precio"], "euros")

    elif opcion == 2:
        nombre = input("Nombre del producto: ")

        existe = False
        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                existe = True

        if existe:
            print("El producto ya existe.")
        else:
            precio = float(input("Precio del producto: "))
            productos.append({
                "nombre": nombre,
                "precio": precio
            })
            print("Producto añadido.")

    elif opcion == 3:
        nombre = input("Nombre del producto que buscas: ")
        encontrado = False

        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                print("Nombre:", producto["nombre"])
                print("Precio:", producto["precio"], "euros")
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == 4:
        nombre = input("Producto que quieres modificar: ")
        encontrado = False

        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                precio = float(input("Nuevo precio: "))
                producto["precio"] = precio
                print("Precio actualizado.")
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == 5:
        nombre = input("Producto que quieres eliminar: ")
        encontrado = False

        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                productos.remove(producto)
                print("Producto eliminado.")
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == 6:
        print("Saliendo de la tienda...")

    else:
        print("Opción no válida.")

print("Programa finalizado.")
