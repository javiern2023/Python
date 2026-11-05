def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura = float(input("Introduce la temperatura: "))

print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Elige una opción: ")

if opcion == "1":
    print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(temperatura))
elif opcion == "2":
    print("Temperatura en Celsius:", fahrenheit_a_celsius(temperatura))
else:
    print("Opción no válida")