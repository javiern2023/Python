class Estudiante:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def aprobado(self):
        return self.nota >= 5


estudiante1 = Estudiante("Pedro", 7)

estudiante1.mostrar_datos()

if estudiante1.aprobado():
    print("El estudiante ha aprobado")
else:
    print("El estudiante ha suspendido")