
agenda = {
    "Ana": "612345678",
    "Luis": "623456789",
    "María": "634567890"
}

nombre = input("Introduce el nombre del contacto que quieres eliminar: ")

if nombre in agenda:
    del agenda[nombre]
    print("Contacto eliminado.")
else:
    print("El contacto no existe.")

print("Agenda final:")

for nombre, telefono in agenda.items():
    print(nombre, ":", telefono)
