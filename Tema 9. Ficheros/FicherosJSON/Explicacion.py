'''
JSON (JavaScript Object Notation) es un formato que permite almacenar información de forma estructurada.

import json Importar el módulo para poder trabajar con el fichero

Para crear un fichero JSON utilizamos open() y la función json.dump().
'''
import json

alumnos = [
    {
        "nombre": "Ana",
        "edad": 20,
        "curso": "Python"
    },
    {
        "nombre": "Luis",
        "edad": 22,
        "curso": "Java"
    }
]

with open("alumnos.json", "w", encoding="utf-8") as fichero:
    json.dump(alumnos, fichero, indent=4, ensure_ascii=False)
'''
"alumnos.json": nombre del fichero.
"w": modo escritura. Si el fichero no existe, lo crea. Si existe, sobrescribe su contenido.
json.dump(): guarda los datos en formato JSON.
indent=4: organiza el contenido con sangrías para facilitar su lectura.
ensure_ascii=False: permite guardar correctamente las tildes y otros caracteres especiales.
'''

# Leer el fichero
with open("alumnos.json", "r", encoding="utf-8") as fichero:
    alumnos = json.load(fichero)

print(alumnos)

'''
Abrimos el fichero en modo lectura ("r").
Utilizamos json.load() para recuperar los datos.
Python convierte automáticamente el contenido JSON en una lista de diccionarios
'''

'''
Insertar:
Leer el fichero.
Crear un nuevo diccionario.
Añadirlo a la lista mediante append().
Guardar nuevamente la lista en el fichero.
append() solamente modifica la lista que tenemos en memoria. Para que el cambio quede guardado 
permanentemente, debemos utilizar nuevamente json.dump().
'''

# Leer el fichero
with open("alumnos.json", "r", encoding="utf-8") as fichero:
    alumnos = json.load(fichero)

# Crear un nuevo alumno
nuevo_alumno = {
    "nombre": "Marta",
    "edad": 21,
    "curso": "Python"
}

# Insertar el alumno en la lista
alumnos.append(nuevo_alumno)

# Guardar los cambios
with open("alumnos.json", "w", encoding="utf-8") as fichero:
    json.dump(alumnos, fichero, indent=4, ensure_ascii=False)


# Consultas
# Buscar por su nombre
with open("alumnos.json", "r", encoding="utf-8") as fichero:
    alumnos = json.load(fichero)

nombre_buscar = input("Introduce el nombre: ")

for alumno in alumnos:
    if alumno["nombre"].lower() == nombre_buscar.lower():
        print("Alumno encontrado")
        print("Nombre:", alumno["nombre"])
        print("Edad:", alumno["edad"])
        print("Curso:", alumno["curso"])

# Todos los alumnos
for alumno in alumnos:
    print(alumno["nombre"], alumno["curso"])

# Los alumnos de un curso en concreto
for alumno in alumnos:
    if alumno["curso"] == "Python":
        print(alumno["nombre"])

# Modificar
'''Leer el fichero.
Buscar el registro que queremos modificar.
Cambiar el valor del campo correspondiente.
Guardar nuevamente el fichero.
'''
with open("alumnos.json", "r", encoding="utf-8") as fichero:
    alumnos = json.load(fichero)

nombre_buscar = input("Nombre del alumno: ")

for alumno in alumnos:
    if alumno["nombre"].lower() == nombre_buscar.lower():

        nueva_edad = int(input("Introduce la nueva edad: "))

        alumno["edad"] = nueva_edad

        print("Edad modificada correctamente.")

        break

# Guardar los cambios
with open("alumnos.json", "w", encoding="utf-8") as fichero:
    json.dump(alumnos, fichero, indent=4, ensure_ascii=False)

# Eliminar
with open("alumnos.json", "r", encoding="utf-8") as fichero:
    alumnos = json.load(fichero)

nombre_eliminar = input("Nombre del alumno que quieres eliminar: ")

for alumno in alumnos:
    if alumno["nombre"].lower() == nombre_eliminar.lower():

        alumnos.remove(alumno)

        print("Alumno eliminado correctamente.")

        break

# Guardar los cambios
with open("alumnos.json", "w", encoding="utf-8") as fichero:
    json.dump(alumnos, fichero, indent=4, ensure_ascii=False)