saldo = 1000

try:
    print("=== CAJERO AUTOMÁTICO ===")
    print("Saldo disponible:", saldo, "euros")

    cantidad = float(input("¿Cuánto dinero quieres retirar? "))

    if cantidad <= 0:
        print("Error: La cantidad debe ser positiva")

    elif cantidad > saldo:
        print("Error: No tienes suficiente saldo")

    else:
        saldo -= cantidad

        print("Retirada realizada correctamente")
        print("Nuevo saldo:", saldo, "euros")

except ValueError:
    print("Error: Debes introducir una cantidad numérica")