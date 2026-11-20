def pedir_numero():
    numero = float(input("Introduce un número: "))
    return numero


def pedir_operacion():
    print("\nOperaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Selecciona una operación: "))
    return opcion