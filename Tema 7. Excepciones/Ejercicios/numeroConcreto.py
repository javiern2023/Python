try:
    numero = int(input("Introduce un número entero: "))

    print("Has introducido el número:", numero)

except ValueError:
    print("Error: Debes introducir un número válido")