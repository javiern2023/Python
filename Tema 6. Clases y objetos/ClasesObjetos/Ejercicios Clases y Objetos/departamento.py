class Empleado:

    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto


class Departamento:

    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print("Departamento:", self.nombre)

        for empleado in self.empleados:
            print(empleado.nombre, "-", empleado.puesto)


empleado1 = Empleado("Ana", "Programadora")
empleado2 = Empleado("Luis", "Diseñador")

departamento1 = Departamento("Informática")

departamento1.agregar_empleado(empleado1)
departamento1.agregar_empleado(empleado2)

departamento1.mostrar_empleados()