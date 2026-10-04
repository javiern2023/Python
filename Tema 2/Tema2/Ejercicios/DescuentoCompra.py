importe = float(input("Introduce el importe de la compra: "))

if importe < 50:
    descuento = 0
elif importe < 100:
    descuento = 5
elif importe < 200:
    descuento = 10
else:
    descuento = 20

importe_descuento = importe * descuento / 100
precio_final = importe - importe_descuento

print(f"Importe original: {importe} €")
print(f"Descuento: {descuento}%")
print(f"Importe descontado: {importe_descuento} €")
print(f"Precio final: {precio_final} €")