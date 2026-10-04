import random

numero_secreto = random.randint(1, 100)

intento = int(input("Adivina el número (1-100): "))

while intento != numero_secreto:

    if intento < numero_secreto:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")

    intento = int(input("Inténtalo de nuevo: "))

print("¡Correcto! Has adivinado el número.")