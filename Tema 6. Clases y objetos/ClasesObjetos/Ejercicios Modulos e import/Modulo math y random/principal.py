import math
import random

numero = float(input("Introduce un número: "))

print("Raíz cuadrada:", math.sqrt(numero))
print("Número redondeado hacia arriba:", math.ceil(numero))
print("Número redondeado hacia abajo:", math.floor(numero))
print("Potencia de 2:", math.pow(numero, 2))

aleatorio = random.randint(1, 100)

print("Número aleatorio entre 1 y 100:", aleatorio)