notas = [5.5, 7.0, 8.5, 6.0, 9.0]

suma = 0

for nota in notas:
    suma += nota

media = suma / len(notas)

print(f"Notas: {notas}")
print(f"Suma: {suma}")
print(f"Media: {media}")