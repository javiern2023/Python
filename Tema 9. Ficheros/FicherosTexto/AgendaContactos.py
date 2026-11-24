
FICHERO = "contactos.txt"


def cargar_contactos():
    contactos = []

    try:
        with open(FICHERO, "r", encoding="utf-8") as fichero:
            for linea in fichero:
                datos = linea.strip().split(";")

                if len(datos) == 4:
                    contacto = {
                        "nombre": datos[0],
                        "telefono": datos[1],
                        "email": datos[2],
                        "ciudad": datos[3]
                    }

                    contactos.append(contacto)

    except FileNotFoundError:
        pass

    return contactos


def guardar_contactos(contactos):
    with open(FICHERO, "w", encoding="utf-8") as fichero:
        for contacto in contactos:
            linea = (f"{contacto['nombre']};"
                     f"{contacto['telefono']};"
                     f"{contacto['email']};"
                     f"{contacto['ciudad']}\n")

            fichero.write(linea)


def anadir_contacto(contactos):
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    email = input("Correo electronico: ")
    ciudad = input("Ciudad: ")

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "ciudad": ciudad
    }

    contactos.append(contacto)
    guardar_contactos(contactos)

    print("Contacto añadido correctamente.")


def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos registrados.")
        return

    for contacto in contactos:
        print("------------------------")
        print("Nombre:", contacto["nombre"])
        print("Telefono:", contacto["telefono"])
        print("Email:", contacto["email"])
        print("Ciudad:", contacto["ciudad"])


def buscar_por_nombre(contactos):
    nombre = input("Nombre a buscar: ").lower()

    encontrada = False

    for contacto in contactos:
        if nombre in contacto["nombre"].lower():
            print(contacto)
            encontrada = True

    if not encontrada:
        print("No se ha encontrado el contacto.")


def buscar_por_ciudad(contactos):
    ciudad = input("Ciudad a buscar: ").lower()

    encontrada = False

    for contacto in contactos:
        if ciudad in contacto["ciudad"].lower():
            print(contacto)
            encontrada = True

    if not encontrada:
        print("No hay contactos de esa ciudad.")


def modificar_telefono(contactos):
    nombre = input("Nombre del contacto: ").lower()

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre:
            nuevo_telefono = input("Nuevo telefono: ")

            contacto["telefono"] = nuevo_telefono

            guardar_contactos(contactos)

            print("Telefono modificado correctamente.")
            return

    print("No se ha encontrado el contacto.")


def eliminar_contacto(contactos):
    nombre = input("Nombre del contacto a eliminar: ").lower()

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre:
            contactos.remove(contacto)
            guardar_contactos(contactos)
            print("Contacto eliminado.")
            return

    print("No se ha encontrado el contacto.")


# PROGRAMA PRINCIPAL

contactos = cargar_contactos()

while True:
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Añadir contacto")
    print("2. Mostrar contactos")
    print("3. Buscar por nombre")
    print("4. Buscar por ciudad")
    print("5. Modificar telefono")
    print("6. Eliminar contacto")
    print("0. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        anadir_contacto(contactos)
    elif opcion == "2":
        mostrar_contactos(contactos)
    elif opcion == "3":
        buscar_por_nombre(contactos)
    elif opcion == "4":
        buscar_por_ciudad(contactos)
    elif opcion == "5":
        modificar_telefono(contactos)
    elif opcion == "6":
        eliminar_contacto(contactos)
    elif opcion == "0":
        print("Fin del programa.")
        break
    else:
        print("Opcion incorrecta.")
