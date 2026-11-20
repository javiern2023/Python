try:
    kilometros = float(input("Introduce los kilómetros: "))

    millas = kilometros * 0.621371

    print("Kilómetros:", kilometros)
    print("Millas:", millas)

except ValueError:
    print("Error: Debes introducir una cantidad numérica")