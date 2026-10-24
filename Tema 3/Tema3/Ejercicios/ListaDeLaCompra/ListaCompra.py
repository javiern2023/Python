
compra = []

while True:
    print("\n===== LISTA DE LA COMPRA =====")
    print("1. Añadir producto")
    print("2. Mostrar lista")
    print("3. Eliminar producto")
    print("4. Modificar producto")
    print("5. Buscar producto")
    print("6. Vaciar lista")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    match opcion:

        case "1":
            producto = input("Introduce el producto que quieres añadir: ")
            compra.append(producto)
            print(f"'{producto}' se ha añadido a la lista.")

        case "2":
            if len(compra) == 0:
                print("La lista de la compra está vacía.")
            else:
                print("\n--- TU LISTA DE LA COMPRA ---")

                for i, producto in enumerate(compra, start=1):
                    print(f"{i}. {producto}")

        case "3":
            if len(compra) == 0:
                print("No hay productos para eliminar.")
            else:
                print("\n--- PRODUCTOS ---")

                for i, producto in enumerate(compra, start=1):
                    print(f"{i}. {producto}")

                try:
                    numero = int(input("Número del producto que quieres eliminar: "))

                    if 1 <= numero <= len(compra):
                        eliminado = compra.pop(numero - 1)
                        print(f"'{eliminado}' se ha eliminado.")
                    else:
                        print("Ese número no existe.")

                except ValueError:
                    print("Debes introducir un número válido.")

        case "4":
            if len(compra) == 0:
                print("No hay productos para modificar.")
            else:
                print("\n--- PRODUCTOS ---")

                for i, producto in enumerate(compra, start=1):
                    print(f"{i}. {producto}")

                try:
                    numero = int(input("Número del producto que quieres modificar: "))

                    if 1 <= numero <= len(compra):
                        nuevo_producto = input("Introduce el nuevo nombre: ")
                        anterior = compra[numero - 1]
                        compra[numero - 1] = nuevo_producto

                        print(f"'{anterior}' se ha cambiado por '{nuevo_producto}'.")

                    else:
                        print("Ese número no existe.")

                except ValueError:
                    print("Debes introducir un número válido.")

        case "5":
            producto = input("¿Qué producto quieres buscar?: ")

            if producto in compra:
                print(f"'{producto}' está en la lista.")
            else:
                print(f"'{producto}' no está en la lista.")

        case "6":
            confirmacion = input("¿Seguro que quieres vaciar la lista? (s/n): ")

            if confirmacion.lower() == "s":
                compra.clear()
                print("La lista se ha vaciado.")
            else:
                print("No se ha eliminado ningún producto.")

        case "0":
            print("¡Hasta la próxima!")
            break

        case _:
            print("Opción no válida. Inténtalo de nuevo.")
