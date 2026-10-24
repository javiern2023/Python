
compra = {}

while True:
    print("\n===== GESTOR DE LA COMPRA =====")
    print("1. Añadir producto")
    print("2. Mostrar productos")
    print("3. Eliminar producto")
    print("4. Modificar producto")
    print("5. Buscar producto")
    print("6. Calcular total de la compra")
    print("7. Vaciar la compra")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    match opcion:

        case "1":
            nombre = input("Nombre del producto: ").strip().lower()

            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue

            if nombre in compra:
                print("Ese producto ya existe en la compra.")
            else:
                try:
                    precio = float(input("Precio por unidad (€): "))
                    cantidad = int(input("Cantidad: "))

                    if precio < 0 or cantidad <= 0:
                        print("El precio no puede ser negativo y la cantidad debe ser mayor que cero.")
                    else:
                        compra[nombre] = {
                            "precio": precio,
                            "cantidad": cantidad
                        }
                        print(f"'{nombre}' añadido correctamente.")

                except ValueError:
                    print("Introduce un precio y una cantidad válidos.")

        case "2":
            if not compra:
                print("La compra está vacía.")
            else:
                print("\n--- LISTA DE LA COMPRA ---")

                for nombre, datos in compra.items():
                    precio = datos["precio"]
                    cantidad = datos["cantidad"]
                    subtotal = precio * cantidad

                    print(
                        f"{nombre.title()} | "
                        f"Precio: {precio:.2f} € | "
                        f"Cantidad: {cantidad} | "
                        f"Subtotal: {subtotal:.2f} €"
                    )

        case "3":
            nombre = input("¿Qué producto quieres eliminar?: ").strip().lower()

            if nombre in compra:
                del compra[nombre]
                print(f"'{nombre}' eliminado correctamente.")
            else:
                print("Ese producto no está en la compra.")

        case "4":
            nombre = input("¿Qué producto quieres modificar?: ").strip().lower()

            if nombre in compra:
                print("1. Modificar precio")
                print("2. Modificar cantidad")

                modificacion = input("Elige qué quieres modificar: ")

                match modificacion:
                    case "1":
                        try:
                            nuevo_precio = float(input("Nuevo precio (€): "))

                            if nuevo_precio < 0:
                                print("El precio no puede ser negativo.")
                            else:
                                compra[nombre]["precio"] = nuevo_precio
                                print("Precio actualizado.")

                        except ValueError:
                            print("Introduce un precio válido.")

                    case "2":
                        try:
                            nueva_cantidad = int(input("Nueva cantidad: "))

                            if nueva_cantidad <= 0:
                                print("La cantidad debe ser mayor que cero.")
                            else:
                                compra[nombre]["cantidad"] = nueva_cantidad
                                print("Cantidad actualizada.")

                        except ValueError:
                            print("Introduce una cantidad válida.")

                    case _:
                        print("Opción de modificación no válida.")

            else:
                print("Ese producto no está en la compra.")

        case "5":
            nombre = input("¿Qué producto quieres buscar?: ").strip().lower()

            if nombre in compra:
                datos = compra[nombre]

                print(f"Producto: {nombre.title()}")
                print(f"Precio: {datos['precio']:.2f} €")
                print(f"Cantidad: {datos['cantidad']}")
                print(
                    f"Subtotal: "
                    f"{datos['precio'] * datos['cantidad']:.2f} €"
                )
            else:
                print("Producto no encontrado.")

        case "6":
            total = 0

            for datos in compra.values():
                total += datos["precio"] * datos["cantidad"]

            print(f"El total de la compra es: {total:.2f} €")

        case "7":
            confirmacion = input(
                "¿Seguro que quieres vaciar la compra? (s/n): "
            ).strip().lower()

            if confirmacion == "s":
                compra.clear()
                print("La compra se ha vaciado.")
            else:
                print("No se ha realizado ningún cambio.")

        case "0":
            print("¡Hasta la próxima!")
            break

        case _:
            print("Opción no válida. Inténtalo de nuevo.")
