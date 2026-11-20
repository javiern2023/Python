try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    print("\nSelecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        resultado = num1 + num2

    elif opcion == 2:
        resultado = num1 - num2

    elif opcion == 3:
        resultado = num1 * num2

    elif opcion == 4:
        resultado = num1 / num2

    else:
        print("Operación no válida")
        resultado = None

    if resultado is not None:
        print("Resultado:", resultado)

except ValueError:
    print("Error: Debes introducir números válidos")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")