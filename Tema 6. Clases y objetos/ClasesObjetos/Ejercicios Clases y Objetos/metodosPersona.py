class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    def edad_futura(self, años):
        return self.edad + años


persona1 = Persona("Ana", 20)

persona1.mostrar_informacion()

print("Edad dentro de 5 años:", persona1.edad_futura(5))