
notas = {
    "Ana": 8.5,
    "Luis": 7.0,
    "María": 9.5,
    "Carlos": 6.0
}

mejor_alumno = max(notas, key=notas.get)

print("El alumno con mejor nota es:", mejor_alumno)
print("Su nota es:", notas[mejor_alumno])
