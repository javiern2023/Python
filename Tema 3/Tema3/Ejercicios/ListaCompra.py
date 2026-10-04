compras = []

while True:
    print()
    print("----- LISTA DE COMPRAS -----")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        producto = input("Introduce el producto: ")
        compras.append(producto)
        print("Producto añadido")

    elif opcion == "2":
        producto = input("Introduce el producto que quieres eliminar: ")

        if producto in compras:
            compras.remove(producto)
            print("Producto eliminado")
        else:
            print("Ese producto no está en la lista")

    elif opcion == "3":
        print("Lista de compras:")

        for producto in compras:
            print(f"- {producto}")

    elif opcion == "4":
        print("Programa terminado")
        break

    else:
        print("Opción no válida")