
total_entradas = 0
recaudacion = 0.0

infantiles = 0
adultos = 0
jubilados = 0

while True:
    print("\n====== CINE PYTHON ======")
    print("1. Comprar entrada")
    print("2. Consultar ventas")
    print("3. Mostrar precios")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            while True:
                print("\n--- TIPO DE ENTRADA ---")
                print("1. Infantil: 5 €")
                print("2. Adulto: 8 €")
                print("3. Jubilado: 6 €")
                print("0. Volver al menú principal")

                tipo = input("Elige el tipo de entrada: ")

                if tipo == "0":
                    break

                match tipo:
                    case "1":
                        precio = 5.0
                    case "2":
                        precio = 8.0
                    case "3":
                        precio = 6.0
                    case _:
                        print("Tipo de entrada incorrecto.")
                        continue

                edad = int(input("Introduce tu edad: "))

                if edad < 0:
                    print("Error: la edad no puede ser negativa.")
                    continue
                elif edad < 12:
                    descuento = 0.10
                elif edad < 65:
                    descuento = 0.0
                else:
                    descuento = 0.15

                importe_descuento = precio * descuento
                total = precio - importe_descuento

                print("\n--- RECIBO ---")

                for i in range(1, 4):
                    if i == 1:
                        print(f"Precio original: {precio:.2f} €")
                    elif i == 2:
                        print(
                            f"Descuento: "
                            f"{importe_descuento:.2f} €"
                        )
                    else:
                        print(f"Total a pagar: {total:.2f} €")

                total_entradas += 1
                recaudacion += total

                match tipo:
                    case "1":
                        infantiles += 1
                    case "2":
                        adultos += 1
                    case "3":
                        jubilados += 1

                print("\nVenta realizada correctamente.")

        case "2":
            print("\n--- RESUMEN DE VENTAS ---")
            print(f"Entradas vendidas: {total_entradas}")
            print(f"Entradas infantiles: {infantiles}")
            print(f"Entradas de adultos: {adultos}")
            print(f"Entradas de jubilados: {jubilados}")
            print(f"Recaudación total: {recaudacion:.2f} €")

        case "3":
            print("\n--- PRECIOS DEL CINE ---")
            print("Entrada infantil: 5.00 €")
            print("Entrada adulto: 8.00 €")
            print("Entrada jubilado: 6.00 €")

        case "0":
            print("Gracias por visitar Cine Python.")
            break

        case _:
            print("Opción incorrecta. Inténtalo de nuevo.")
