precio = float(input("Introduce el precio del producto: "))
iva = float(input("Introduce el IVA (%): "))

importe_iva = precio * iva / 100
precio_final = precio + importe_iva

print(f"Precio sin IVA: {precio} €")
print(f"IVA: {importe_iva} €")
print(f"Precio final: {precio_final} €")