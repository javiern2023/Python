saldo = float(input("Introduce el saldo disponible: "))
cantidad = float(input("Introduce la cantidad que quieres retirar: "))

if cantidad <= 0:
    print("La cantidad debe ser mayor que cero")
elif cantidad > saldo:
    print("Saldo insuficiente")
else:
    saldo = saldo - cantidad

    print("Retirada realizada correctamente")
    print(f"Has retirado: {cantidad} €")
    print(f"Saldo restante: {saldo} €")