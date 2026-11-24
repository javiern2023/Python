
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="uax"
)

cursor = conexion.cursor()


# INSERTAR ALUMNO
def insertar_alumno():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    email = input("Email: ")

    sql = """
        INSERT INTO alumnos (nombre, edad, email)
        VALUES (%s, %s, %s)
    """

    valores = (nombre, edad, email)

    cursor.execute(sql, valores)
    conexion.commit()

    print("Alumno insertado correctamente")


# CONSULTAR ALUMNOS
def consultar_alumnos():
    sql = "SELECT * FROM alumnos"

    cursor.execute(sql)
    resultados = cursor.fetchall()

    for alumno in resultados:
        print("----------------------")
        print("ID:", alumno[0])
        print("Nombre:", alumno[1])
        print("Edad:", alumno[2])
        print("Email:", alumno[3])


# MODIFICAR ALUMNO
def modificar_alumno():
    id = int(input("ID del alumno: "))
    nombre = input("Nuevo nombre: ")
    edad = int(input("Nueva edad: "))
    email = input("Nuevo email: ")

    sql = """
        UPDATE alumnos
        SET nombre = %s,
            edad = %s,
            email = %s
        WHERE id = %s
    """

    valores = (nombre, edad, email, id)

    cursor.execute(sql, valores)
    conexion.commit()

    if cursor.rowcount > 0:
        print("Alumno modificado correctamente")
    else:
        print("Alumno no encontrado")


# ELIMINAR ALUMNO
def eliminar_alumno():
    id = int(input("ID del alumno: "))

    sql = "DELETE FROM alumnos WHERE id = %s"

    cursor.execute(sql, (id,))
    conexion.commit()

    if cursor.rowcount > 0:
        print("Alumno eliminado correctamente")
    else:
        print("Alumno no encontrado")


# MENÚ PRINCIPAL
try:
    while True:
        print("\n===== GESTIÓN DE ALUMNOS =====")
        print("1. Insertar alumno")
        print("2. Consultar alumnos")
        print("3. Modificar alumno")
        print("4. Eliminar alumno")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            insertar_alumno()

        elif opcion == "2":
            consultar_alumnos()

        elif opcion == "3":
            modificar_alumno()

        elif opcion == "4":
            eliminar_alumno()

        elif opcion == "0":
            print("Saliendo del programa")
            break

        else:
            print("Opción incorrecta")

except mysql.connector.Error as e:
    print("Error de MySQL:", e)

finally:
    cursor.close()
    conexion.close()
    print("Conexión cerrada")
