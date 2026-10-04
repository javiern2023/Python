segundos_totales = int(input("Introduce una cantidad de segundos: "))

horas = segundos_totales // 3600  #División entera
resto = segundos_totales % 3600   # Resto
minutos = resto // 60
segundos = resto % 60

print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")