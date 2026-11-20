class Empleado:

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Salario:", self.salario, "euros")


class EmpleadoFijo(Empleado):

    def __init__(self, nombre, salario, antiguedad):
        super().__init__(nombre, salario)
        self.antiguedad = antiguedad

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Antigüedad:", self.antiguedad, "años")


class EmpleadoTemporal(Empleado):

    def __init__(self, nombre, salario, duracion):
        super().__init__(nombre, salario)
        self.duracion = duracion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Duración del contrato:", self.duracion, "meses")


empleado1 = EmpleadoFijo("Carlos", 2500, 5)

empleado2 = EmpleadoTemporal("Laura", 1800, 6)

print("=== EMPLEADO FIJO ===")
empleado1.mostrar_informacion()

print("\n=== EMPLEADO TEMPORAL ===")
empleado2.mostrar_informacion()