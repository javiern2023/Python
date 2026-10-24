
notas = {
    "Ana": [8, 9, 10],
    "Luis": [6, 7, 8],
    "María": [9, 10, 9]
}

nombre = input("Introduce el nombre del alumno: ")

if nombre in notas:
    media = sum(notas[nombre]) / len(notas[nombre])
    print("La media de", nombre, "es:", media)
else:
    print("El alumno no existe.")
