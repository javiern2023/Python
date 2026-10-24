
while True:
    print("\n====== MENÚ DE CONTADORES ======")
    print("1. Contar desde un número hasta 100")
    print("2. Contar los números pares desde 1 hasta un número")
    print("3. Cuenta atrás desde un número hasta 0")
    print("0. Salir")
    print("================================")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            numero = int(input("Introduce un número entre 1 y 100: "))

            if numero < 1 or numero > 100:
                print("Error: el número debe estar entre 1 y 100.")
            else:
                for i in range(numero, 101):
                    print(i)

        case "2":
            numero = int(input("Introduce un número positivo: "))

            if numero < 1:
                print("Error: debes introducir un número mayor que 0.")
            else:
                for i in range(2, numero + 1, 2):
                    print(i)

        case "3":
            numero = int(input("Introduce un número positivo o cero: "))

            if numero < 0:
                print("Error: el número no puede ser negativo.")
            else:
                for i in range(numero, -1, -1):
                    print(i)

        case "0":
            print("Has salido del programa. ¡Hasta pronto!")
            break

        case _:
            print("Opción incorrecta. Elige una opción del 0 al 3.")
