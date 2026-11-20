class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona1 = Persona("Carlos", 25)

print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)