numeros = []

while True:
    print()
    print("----- GESTIÓN DE LISTA -----")
    print("1. Añadir número")
    print("2. Eliminar número")
    print("3. Buscar número")
    print("4. Mostrar números")
    print("5. Mostrar mayor")
    print("6. Mostrar menor")
    print("7. Mostrar suma")
    print("8. Vaciar lista")
    print("9. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        numero = float(input("Introduce un número: "))
        numeros.append(numero)
        print("Número añadido")

    elif opcion == "2":
        numero = float(input("Introduce el número que quieres eliminar: "))

        if numero in numeros:
            numeros.remove(numero)
            print("Número eliminado")
        else:
            print("El número no está en la lista")

    elif opcion == "3":
        numero = float(input("Introduce el número que quieres buscar: "))

        if numero in numeros:
            print("El número está en la lista")
        else:
            print("El número no está en la lista")

    elif opcion == "4":
        if len(numeros) == 0:
            print("La lista está vacía")
        else:
            print("Números:")

            for numero in numeros:
                print(numero)

    elif opcion == "5":
        if len(numeros) == 0:
            print("La lista está vacía")
        else:
            print(f"El número mayor es: {max(numeros)}")

    elif opcion == "6":
        if len(numeros) == 0:
            print("La lista está vacía")
        else:
            print(f"El número menor es: {min(numeros)}")

    elif opcion == "7":
        if len(numeros) == 0:
            print("La lista está vacía")
        else:
            print(f"La suma es: {sum(numeros)}")

    elif opcion == "8":
        numeros.clear()
        print("Lista vaciada")

    elif opcion == "9":
        print("Programa terminado")
        break

    else:
        print("Opción no válida")