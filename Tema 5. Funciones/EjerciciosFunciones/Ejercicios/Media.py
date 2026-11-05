def calcular_media(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Introduce la primera nota: "))
num2 = float(input("Introduce la segunda nota: "))
num3 = float(input("Introduce la tercera nota: "))

media = calcular_media(num1, num2, num3)

print("La media es:", media)