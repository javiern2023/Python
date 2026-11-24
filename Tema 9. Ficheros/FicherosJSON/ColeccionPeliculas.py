
import json

FICHERO = "peliculas.json"


def cargar_peliculas():
    try:
        with open(FICHERO, "r", encoding="utf-8") as fichero:
            return json.load(fichero)

    except FileNotFoundError:
        return []


def guardar_peliculas(peliculas):
    with open(FICHERO, "w", encoding="utf-8") as fichero:
        json.dump(peliculas, fichero, indent=4, ensure_ascii=False)


def anadir_pelicula(peliculas):
    titulo = input("Titulo: ")
    director = input("Director: ")
    anio = int(input("Año de estreno: "))
    genero = input("Genero: ")
    valoracion = float(input("Valoracion (0-10): "))

    pelicula = {
        "titulo": titulo,
        "director": director,
        "anio": anio,
        "genero": genero,
        "valoracion": valoracion
    }

    peliculas.append(pelicula)
    guardar_peliculas(peliculas)

    print("Pelicula añadida correctamente.")


def mostrar_peliculas(peliculas):
    if not peliculas:
        print("No hay peliculas registradas.")
        return

    for pelicula in peliculas:
        print("------------------------")
        print("Titulo:", pelicula["titulo"])
        print("Director:", pelicula["director"])
        print("Año:", pelicula["anio"])
        print("Genero:", pelicula["genero"])
        print("Valoracion:", pelicula["valoracion"])


def buscar_por_titulo(peliculas):
    titulo = input("Introduce el titulo: ").lower()

    encontrada = False

    for pelicula in peliculas:
        if titulo in pelicula["titulo"].lower():
            print(pelicula)
            encontrada = True

    if not encontrada:
        print("No se ha encontrado ninguna pelicula.")


def buscar_por_director(peliculas):
    director = input("Introduce el director: ").lower()

    encontrada = False

    for pelicula in peliculas:
        if director in pelicula["director"].lower():
            print(pelicula)
            encontrada = True

    if not encontrada:
        print("No se han encontrado peliculas de ese director.")


def buscar_por_anio(peliculas):
    anio = int(input("Introduce el año: "))

    encontrada = False

    for pelicula in peliculas:
        if pelicula["anio"] == anio:
            print(pelicula)
            encontrada = True

    if not encontrada:
        print("No hay peliculas de ese año.")


def eliminar_pelicula(peliculas):
    titulo = input("Titulo de la pelicula a eliminar: ").lower()

    for pelicula in peliculas:
        if pelicula["titulo"].lower() == titulo:
            peliculas.remove(pelicula)
            guardar_peliculas(peliculas)
            print("Pelicula eliminada.")
            return

    print("No se ha encontrado la pelicula.")


# PROGRAMA PRINCIPAL

peliculas = cargar_peliculas()

while True:
    print("\n--- GESTION DE PELICULAS ---")
    print("1. Añadir pelicula")
    print("2. Mostrar peliculas")
    print("3. Buscar por titulo")
    print("4. Buscar por director")
    print("5. Buscar por año")
    print("6. Eliminar pelicula")
    print("0. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        anadir_pelicula(peliculas)
    elif opcion == "2":
        mostrar_peliculas(peliculas)
    elif opcion == "3":
        buscar_por_titulo(peliculas)
    elif opcion == "4":
        buscar_por_director(peliculas)
    elif opcion == "5":
        buscar_por_anio(peliculas)
    elif opcion == "6":
        eliminar_pelicula(peliculas)
    elif opcion == "0":
        print("Fin del programa.")
        break
    else:
        print("Opcion incorrecta.")
