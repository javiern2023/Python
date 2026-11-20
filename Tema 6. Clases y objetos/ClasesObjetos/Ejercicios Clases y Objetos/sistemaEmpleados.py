class Empleado:

    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Puesto:", self.puesto)
        print("Salario:", self.salario, "euros")


empleado1 = Empleado("Antonio", "Programador", 2500)

empleado1.mostrar_informacion()