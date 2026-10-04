numeros = [10, -5, 20, -8, 0, 15, -3, 7]

positivos = 0
negativos = 0

for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")