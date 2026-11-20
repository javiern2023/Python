from excepciones import PasswordInvalidaError


def validar_password(password):

    if password == "":
        raise PasswordInvalidaError("La contraseña no puede estar vacía")

    if len(password) < 8:
        raise PasswordInvalidaError("La contraseña debe tener al menos 8 caracteres")

    if not any(caracter.isdigit() for caracter in password):
        raise PasswordInvalidaError("La contraseña debe contener al menos un número")

    return True