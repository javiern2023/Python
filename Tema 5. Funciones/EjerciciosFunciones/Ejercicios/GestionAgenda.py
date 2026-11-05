agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto añadido correctamente")

def mostrar_agenda():
    if len(agenda) == 0:
        print("La agenda está vacía")
    else:
        for nombre, telefono in agenda.items():
            print(nombre, ":", telefono)

def buscar_contacto(nombre):
    if nombre in agenda:
        print("Teléfono:", agenda[nombre])
    else:
        print("Contacto no encontrado")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado")
    else:
        print("Contacto no encontrado")

while True:
    print("\n--- AGENDA ---")
    print("1. Añadir contacto")
    print("2. Mostrar agenda")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agregar_contacto(nombre, telefono)

    elif opcion == "2":
        mostrar_agenda()

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        buscar_contacto(nombre)

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")
        eliminar_contacto(nombre)

    elif opcion == "5":
        print("Saliendo de la agenda...")
        break

    else:
        print("Opción no válida")