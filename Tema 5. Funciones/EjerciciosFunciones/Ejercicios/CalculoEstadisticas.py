def calcular_estadisticas(lista):
    suma = sum(lista)
    media = suma / len(lista)
    mayor = max(lista)
    menor = min(lista)

    print("Suma:", suma)
    print("Media:", media)
    print("Mayor:", mayor)
    print("Menor:", menor)

numeros = [10, 20, 30, 40, 50]

calcular_estadisticas(numeros)