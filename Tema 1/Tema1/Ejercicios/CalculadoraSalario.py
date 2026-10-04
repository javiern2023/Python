salario_mensual = float(input("Introduce tu salario mensual: "))

salario_anual = salario_mensual * 12

subida = salario_anual * 5 / 100
salario_anual_nuevo = salario_anual + subida

salario_mensual_nuevo = salario_anual_nuevo / 12

print(f"Salario mensual actual: {salario_mensual} €")
print(f"Salario anual actual: {salario_anual} €")
print(f"Subida anual: {subida} €")
print(f"Salario anual con subida: {salario_anual_nuevo} €")
print(f"Nuevo salario mensual: {salario_mensual_nuevo} €")