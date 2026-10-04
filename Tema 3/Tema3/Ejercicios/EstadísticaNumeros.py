numeros = [10, 15, 22, 31, 40, 51, 64]

maximo = max(numeros)
minimo = min(numeros)

suma = 0
pares = 0
impares = 0

for numero in numeros:
    suma += numero

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

media = suma / len(numeros)

print(f"Lista: {numeros}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Media: {media}")
print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")