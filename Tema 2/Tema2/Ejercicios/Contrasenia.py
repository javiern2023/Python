contraseña_correcta = "python123"

contraseña = input("Introduce la contraseña: ")

while contraseña != contraseña_correcta:
    print("Contraseña incorrecta")
    contraseña = input("Introduce la contraseña: ")

print("Contraseña correcta")