from validador import validar_password
from excepciones import PasswordInvalidaError


try:

    password = input("Introduce una contraseña: ")

    validar_password(password)

    print("Contraseña válida")

except PasswordInvalidaError as error:

    print("Error:", error)