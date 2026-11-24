
import json
import os

FICHERO = "videojuegos.json"


# --------------------------------
# FUNCION PARA CARGAR LOS DATOS
# --------------------------------

def cargar_videojuegos():

    if not os.path.exists(FICHERO):
        return []

    with open(FICHERO, "r", encoding="utf-8") as fichero:
        videojuegos = json.load(fichero)

    return videojuegos


# --------------------------------
# FUNCION PARA GUARDAR LOS DATOS
# --------------------------------

def guardar_videojuegos(videojuegos):

    with open(FICHERO, "w", encoding="utf-8") as fichero:
        json.dump(videojuegos, fichero, indent=4, ensure_ascii=False)


# --------------------------------
# FUNCION PARA AÑADIR VIDEOJUEGOS
# --------------------------------

def anadir_videojuego(videojuegos):

    print("\n--- AÑADIR VIDEOJUEGO ---")

    titulo = input("Título: ")
    plataforma = input("Plataforma: ")
    anio = int(input("Año de lanzamiento: "))
    precio = float(input("Precio: "))

    if videojuegos:
        identificador = max(v["id"] for v in videojuegos) + 1
    else:
        identificador = 1

    videojuego = {
        "id": identificador,
        "titulo": titulo,
        "plataforma": plataforma,
        "anio": anio,
        "precio": precio
    }

    videojuegos.append(videojuego)

    guardar_videojuegos(videojuegos)

    print("Videojuego añadido correctamente.")


# --------------------------------
# FUNCION PARA MOSTRAR VIDEOJUEGOS
# --------------------------------

def mostrar_videojuegos(videojuegos):

    print("\n--- LISTADO DE VIDEOJUEGOS ---")

    if not videojuegos:
        print("No hay videojuegos registrados.")
        return

    for videojuego in videojuegos:

        print("-----------------------------")
        print("ID:", videojuego["id"])
        print("Título:", videojuego["titulo"])
        print("Plataforma:", videojuego["plataforma"])
        print("Año:", videojuego["anio"])
        print("Precio:", videojuego["precio"], "euros")


# --------------------------------
# FUNCION PARA BUSCAR POR TITULO
# --------------------------------

def buscar_videojuego(videojuegos):

    print("\n--- BUSCAR VIDEOJUEGO ---")

    titulo = input("Introduce el título: ").lower()

    encontrado = False

    for videojuego in videojuegos:

        if titulo in videojuego["titulo"].lower():

            print("-----------------------------")
            print("ID:", videojuego["id"])
            print("Título:", videojuego["titulo"])
            print("Plataforma:", videojuego["plataforma"])
            print("Año:", videojuego["anio"])
            print("Precio:", videojuego["precio"], "euros")

            encontrado = True

    if not encontrado:
        print("No se ha encontrado ningún videojuego.")


# --------------------------------
# FUNCION PARA BUSCAR POR PLATAFORMA
# --------------------------------

def buscar_por_plataforma(videojuegos):

    print("\n--- BUSCAR POR PLATAFORMA ---")

    plataforma = input("Introduce la plataforma: ").lower()

    encontrado = False

    for videojuego in videojuegos:

        if videojuego["plataforma"].lower() == plataforma:

            print(videojuego)

            encontrado = True

    if not encontrado:
        print("No hay videojuegos de esa plataforma.")


# --------------------------------
# FUNCION PARA MODIFICAR EL PRECIO
# --------------------------------

def modificar_precio(videojuegos):

    print("\n--- MODIFICAR PRECIO ---")

    identificador = int(input("Introduce el ID del videojuego: "))

    for videojuego in videojuegos:

        if videojuego["id"] == identificador:

            nuevo_precio = float(input("Introduce el nuevo precio: "))

            videojuego["precio"] = nuevo_precio

            guardar_videojuegos(videojuegos)

            print("Precio modificado correctamente.")

            return

    print("No existe ningún videojuego con ese ID.")


# --------------------------------
# FUNCION PARA ELIMINAR VIDEOJUEGOS
# --------------------------------

def eliminar_videojuego(videojuegos):

    print("\n--- ELIMINAR VIDEOJUEGO ---")

    identificador = int(input("Introduce el ID del videojuego: "))

    for videojuego in videojuegos:

        if videojuego["id"] == identificador:

            videojuegos.remove(videojuego)

            guardar_videojuegos(videojuegos)

            print("Videojuego eliminado correctamente.")

            return

    print("No existe ningún videojuego con ese ID.")


# --------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------

videojuegos = cargar_videojuegos()

while True:

    print("\n================================")
    print("   BIBLIOTECA DE VIDEOJUEGOS")
    print("================================")
    print("1. Añadir videojuego")
    print("2. Mostrar videojuegos")
    print("3. Buscar videojuego por título")
    print("4. Buscar videojuegos por plataforma")
    print("5. Modificar precio")
    print("6. Eliminar videojuego")
    print("0. Salir")
    print("================================")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        anadir_videojuego(videojuegos)

    elif opcion == "2":
        mostrar_videojuegos(videojuegos)

    elif opcion == "3":
        buscar_videojuego(videojuegos)

    elif opcion == "4":
        buscar_por_plataforma(videojuegos)

    elif opcion == "5":
        modificar_precio(videojuegos)

    elif opcion == "6":
        eliminar_videojuego(videojuegos)

    elif opcion == "0":
        print("Gracias por utilizar la aplicación.")
        break

    else:
        print("Opción incorrecta.")