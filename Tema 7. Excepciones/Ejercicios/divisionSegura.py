try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = num1 / num2

    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")