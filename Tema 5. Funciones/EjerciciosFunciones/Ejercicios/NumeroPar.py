def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Introduce un número: "))

if es_par(num):
    print("El número es par")
else:
    print("El número es impar")