agenda = {
    "Ana": "600123456",
    "Luis": "600654321",
    "Carlos": "600987654"
}

try:
    nombre = input("Introduce el nombre que quieres buscar: ")

    print("Teléfono:", agenda[nombre])

except KeyError:
    print("Error: El contacto no existe")


try:
    nombre = input("\nIntroduce el contacto que quieres eliminar: ")

    del agenda[nombre]

    print("Contacto eliminado correctamente")

except KeyError:
    print("Error: No existe ese contacto")

print("\nAgenda actualizada:")
print(agenda)