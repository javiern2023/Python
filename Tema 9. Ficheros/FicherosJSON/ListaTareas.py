
import json

FICHERO = "tareas.json"


def cargar_tareas():
    try:
        with open(FICHERO, "r", encoding="utf-8") as fichero:
            return json.load(fichero)

    except FileNotFoundError:
        return []


def guardar_tareas(tareas):
    with open(FICHERO, "w", encoding="utf-8") as fichero:
        json.dump(tareas, fichero, indent=4, ensure_ascii=False)


def anadir_tarea(tareas):
    descripcion = input("Descripcion de la tarea: ")

    if tareas:
        identificador = max(t["id"] for t in tareas) + 1
    else:
        identificador = 1

    tarea = {
        "id": identificador,
        "descripcion": descripcion,
        "estado": "Pendiente"
    }

    tareas.append(tarea)
    guardar_tareas(tareas)
    print("Tarea añadida correctamente.")


def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return

    for tarea in tareas:
        print(f"{tarea['id']} - {tarea['descripcion']} "
              f"- {tarea['estado']}")


def buscar_tarea(tareas):
    descripcion = input("Descripcion a buscar: ").lower()

    encontrada = False

    for tarea in tareas:
        if descripcion in tarea["descripcion"].lower():
            print(tarea)
            encontrada = True

    if not encontrada:
        print("No se ha encontrado ninguna tarea.")


def completar_tarea(tareas):
    identificador = int(input("Introduce el ID de la tarea: "))

    for tarea in tareas:
        if tarea["id"] == identificador:
            tarea["estado"] = "Completada"
            guardar_tareas(tareas)
            print("Tarea completada.")
            return

    print("No existe una tarea con ese ID.")


def eliminar_tarea(tareas):
    identificador = int(input("Introduce el ID de la tarea: "))

    for tarea in tareas:
        if tarea["id"] == identificador:
            tareas.remove(tarea)
            guardar_tareas(tareas)
            print("Tarea eliminada.")
            return

    print("No existe una tarea con ese ID.")


# PROGRAMA PRINCIPAL

tareas = cargar_tareas()

while True:
    print("\n--- GESTION DE TAREAS ---")
    print("1. Añadir tarea")
    print("2. Mostrar tareas")
    print("3. Buscar tarea")
    print("4. Completar tarea")
    print("5. Eliminar tarea")
    print("0. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        anadir_tarea(tareas)
    elif opcion == "2":
        mostrar_tareas(tareas)
    elif opcion == "3":
        buscar_tarea(tareas)
    elif opcion == "4":
        completar_tarea(tareas)
    elif opcion == "5":
        eliminar_tarea(tareas)
    elif opcion == "0":
        print("Fin del programa.")
        break
    else:
        print("Opcion incorrecta.")
