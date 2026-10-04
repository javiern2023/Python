agenda = []

while True:
    print()
    print("----- AGENDA -----")
    print("1. Añadir nombre")
    print("2. Buscar nombre")
    print("3. Eliminar nombre")
    print("4. Mostrar nombres")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Introduce el nombre: ")
        agenda.append(nombre)
        print("Nombre añadido")

    elif opcion == "2":
        nombre = input("Introduce el nombre que quieres buscar: ")

        if nombre in agenda:
            print("El nombre está en la agenda")
        else:
            print("El nombre no está en la agenda")

    elif opcion == "3":
        nombre = input("Introduce el nombre que quieres eliminar: ")

        if nombre in agenda:
            agenda.remove(nombre)
            print("Nombre eliminado")
        else:
            print("El nombre no existe")

    elif opcion == "4":
        if len(agenda) == 0:
            print("La agenda está vacía")
        else:
            print("Nombres:")

            for nombre in agenda:
                print(f"- {nombre}")

    elif opcion == "5":
        print("Programa terminado")
        break

    else:
        print("Opción no válida")