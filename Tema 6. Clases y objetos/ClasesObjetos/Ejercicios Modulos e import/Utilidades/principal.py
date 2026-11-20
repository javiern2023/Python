import utilidades

numero = int(input("Introduce un número: "))

if utilidades.es_positivo(numero):
    print("El número es positivo")
else:
    print("El número no es positivo")

if utilidades.es_par(numero):
    print("El número es par")
else:
    print("El número es impar")

edad = int(input("Introduce tu edad: "))

if utilidades.validar_edad(edad):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")