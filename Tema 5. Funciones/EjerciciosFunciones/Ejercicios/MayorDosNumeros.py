def mayor(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Los dos números son iguales"

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print("El resultado es:", mayor(num1, num2))