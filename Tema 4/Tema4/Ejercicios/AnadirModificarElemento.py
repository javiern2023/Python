
agenda = {
    "Ana": "612345678",
    "Luis": "623456789"
}

nombre = input("Introduce el nombre del contacto: ")
telefono = input("Introduce el teléfono: ")

if nombre in agenda:
    agenda[nombre] = telefono
    print("Contacto modificado.")
else:
    agenda[nombre] = telefono
    print("Contacto añadido.")

print("Agenda actualizada:")

for nombre, telefono in agenda.items():
    print(nombre, ":", telefono)
