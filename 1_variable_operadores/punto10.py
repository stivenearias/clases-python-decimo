"""
Pide al usuario la base y altura de un triángulo, 
calcula su área (base × altura / 2) y muestra el resultado.
"""
# Declarar variables
base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))

# Calcular area del triangulo
area = (base * altura) / 2

# Mostrar resultado
print(f"El area del triangulo con base {base} y altura {altura} es: {int(area)}")