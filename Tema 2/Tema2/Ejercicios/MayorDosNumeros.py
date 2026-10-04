numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

if numero1 > numero2:
    print(f"El mayor es {numero1}")
elif numero2 > numero1:
    print(f"El mayor es {numero2}")
else:
    print("Los dos números son iguales")