#1. AÑADIR PRODUCTO

def añadir_producto(compra):

    # Elimina espacios en blanco
    nombre = input("Introduce el nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío")
        return

    cantidad = int(input("Introduce la cantidad: "))

    # Generamos un código nuevo
    if len(compra) == 0:
        codigo = 1
    else:
        # Obtenemos el mayor elemento clave y le sumamos uno
        codigo = max(compra.keys()) + 1

    # Creamos el diccionario del producto
    producto = {
        "nombre": nombre,
        "cantidad": cantidad
    }

    # Guardamos el producto en el diccionario principal
    compra[codigo] = producto

    print("Producto añadido correctamente")


# 2. MOSTRAR LISTA DE LA COMPRA

def mostrar_lista(compra):

    if len(compra) == 0:
        print("La lista de la compra está vacía")

    else:

        print("\n===== LISTA DE LA COMPRA =====")

        for codigo, producto in compra.items():

            print("Código:", codigo)
            print("Nombre:", producto["nombre"])
            print("Cantidad:", producto["cantidad"])
            print("-----------------------------")


# 3. ELIMINAR PRODUCTO

def eliminar_producto(compra):

    codigo = int(input("Introduce el código del producto: "))

    if codigo in compra:

        del compra[codigo]

        print("Producto eliminado correctamente")

    else:

        print("No existe ningún producto con ese código")


# 4. MODIFICAR PRODUCTO

def modificar_producto(compra):

    codigo = int(input("Introduce el código del producto: "))

    if codigo in compra:

        print("Producto actual:", compra[codigo])

        nombre = input("Introduce el nuevo nombre: ").strip()
        cantidad = int(input("Introduce la nueva cantidad: "))

        compra[codigo]["nombre"] = nombre
        compra[codigo]["cantidad"] = cantidad

        print("Producto modificado correctamente")

    else:

        print("No existe ningún producto con ese código")


# 5. BUSCAR PRODUCTO

def buscar_producto(compra):

    nombre = input("Introduce el nombre que quieres buscar: ").strip()

    encontrados = []

    for codigo, producto in compra.items():

        if producto["nombre"].lower() == nombre.lower():

            encontrados.append((codigo, producto))

    return encontrados


# 6. VACIAR LISTA

def vaciar_lista(compra):

    compra.clear()

    print("La lista de la compra está vacía")


# 7. MENÚ PRINCIPAL

def menu():

    # Diccionario principal
    compra = {}

    opcion = -1

    while opcion != 0:

        print("\n===== LISTA DE LA COMPRA =====")
        print("1. Añadir producto")
        print("2. Mostrar lista de la compra")
        print("3. Eliminar producto")
        print("4. Modificar producto")
        print("5. Buscar producto")
        print("6. Vaciar lista")
        print("0. Salir")

        opcion = int(input("\nElige una opción: "))

        match opcion:

            case 1:
                añadir_producto(compra)

            case 2:
                mostrar_lista(compra)

            case 3:
                eliminar_producto(compra)

            case 4:
                modificar_producto(compra)

            case 5:

                resultados = buscar_producto(compra)

                if len(resultados) > 0:

                    print("\nProductos encontrados:")

                    for codigo, producto in resultados:

                        print("Código:", codigo)
                        print("Nombre:", producto["nombre"])
                        print("Cantidad:", producto["cantidad"])

                else:

                    print("Producto no encontrado")

            case 6:
                vaciar_lista(compra)

            case 0:
                print("Saliendo del programa...")

            case _:
                print("Opción incorrecta")


# ==========================================
# INICIO DEL PROGRAMA
# ==========================================

menu()
