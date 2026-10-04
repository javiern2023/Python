notas = [5.5, 7.0, 8.5, 6.0, 9.0]

print("Notas actuales:")

for i in range(len(notas)):
    print(f"{i + 1}. {notas[i]}")

posicion = int(input("¿Qué nota quieres modificar? "))

nueva_nota = float(input("Introduce la nueva nota: "))

notas[posicion - 1] = nueva_nota

print("Notas modificadas:")

for i in range(len(notas)):
    print(f"{i + 1}. {notas[i]}")