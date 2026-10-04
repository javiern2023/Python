numeros = [45, 12, 78, 3, 56, 23]

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print(f"El número mayor es: {mayor}")