def buscar_elemento(lista, elemento):
    if elemento in lista:
        return True
    else:
        return False

numeros = [10, 20, 30, 40, 50]

buscar = int(input("Introduce el número que quieres buscar: "))

if buscar_elemento(numeros, buscar):
    print("El número está en la lista")
else:
    print("El número no está en la lista")