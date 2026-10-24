
saldo = 1000.0
ingresos = 0
retiradas = 0

while True:
    print("\n====== CAJERO AUTOMÁTICO ======")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar resumen de operaciones")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            print(f"Tu saldo actual es: {saldo:.2f} €")

        case "2":
            cantidad = float(input("¿Cuánto dinero quieres ingresar?: "))

            if cantidad > 0:
                saldo += cantidad
                ingresos += 1
                print("Ingreso realizado correctamente.")
                print(f"Tu saldo actual es: {saldo:.2f} €")
            else:
                print("Error: la cantidad debe ser mayor que cero.")

        case "3":
            cantidad = float(input("¿Cuánto dinero quieres retirar?: "))

            if cantidad <= 0:
                print("Error: la cantidad debe ser mayor que cero.")
            elif cantidad > saldo:
                print("Error: no tienes suficiente saldo.")
            else:
                print("Procesando retirada...")

                for i in range(3, 0, -1):
                    print(i)

                saldo -= cantidad
                retiradas += 1

                print("Retirada realizada correctamente.")
                print(f"Tu saldo actual es: {saldo:.2f} €")

        case "4":
            print("\n--- RESUMEN DE OPERACIONES ---")
            print(f"Número de ingresos: {ingresos}")
            print(f"Número de retiradas: {retiradas}")
            print(f"Saldo actual: {saldo:.2f} €")

        case "0":
            print("Gracias por utilizar nuestro cajero.")
            break

        case _:
            print("Opción incorrecta. Inténtalo de nuevo.")
