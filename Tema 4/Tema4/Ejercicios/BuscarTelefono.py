
agenda = {
    "Ana": "612345678",
    "Luis": "623456789",
    "María": "634567890"
}

nombre = input("Introduce el nombre del contacto: ")

if nombre in agenda:
    print("Teléfono:", agenda[nombre])
else:
    print("El contacto no existe.")
