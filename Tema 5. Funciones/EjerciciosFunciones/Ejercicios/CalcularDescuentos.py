def calcular_descuento(precio, descuento):
    cantidad_descuento = precio * descuento / 100
    precio_final = precio - cantidad_descuento
    return precio_final

precio = float(input("Introduce el precio del producto: "))
descuento = float(input("Introduce el descuento (%): "))

resultado = calcular_descuento(precio, descuento)

print("El precio final es:", resultado, "euros")