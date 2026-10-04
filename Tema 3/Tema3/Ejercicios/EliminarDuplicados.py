numeros = [10, 20, 10, 30, 20, 40, 10, 50]

sin_duplicados = []

for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print(f"Lista original: {numeros}")
print(f"Lista sin duplicados: {sin_duplicados}")