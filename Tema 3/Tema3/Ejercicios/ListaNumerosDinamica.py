numeros = []

while True:
    entrada = input("Introduce un número (o escribe 'fin' para terminar): ")

    if entrada.lower() == "fin":
        break

    numero = float(entrada)
    numeros.append(numero)

print(f"Lista: {numeros}")
print(f"Cantidad de números: {len(numeros)}")
print(f"Suma: {sum(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")