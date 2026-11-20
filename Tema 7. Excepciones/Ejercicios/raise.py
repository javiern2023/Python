try:
    numero = int(input("Introduce un número: "))

    resultado = 100 / numero

    print("Resultado:", resultado)

except ValueError:
    print("Error: Debes introducir un número")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

finally:
    print("El programa ha finalizado")