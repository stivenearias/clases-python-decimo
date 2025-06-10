"""
2.	Crear un programa que ingresados 3 numeros haga lo siguiente:
a.	Sumar el numero 1 con el numero 2 y decir si es multiplo de 2
b.	Mostrar el promedio de los 3 numeros
c.	Restar el numero 2 con el numero 3 y decir si es un numero positivo
"""

# Solicitar el ingreso de tres números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Resolver punto a
suma = numero1 + numero2
multiplo = suma % 2 == 0

# Respuesta punto a
print("¿La suma del numero 1 con el numero 2 es multiplo de 2?", multiplo)

# Resolver punto b
promedio = (numero1 + numero2 + numero3) / 3

# Mostrar el resultado de b
print("El promedio de los 3 numeros es:", promedio)

# Punto c
resta = numero2 - numero3
positivo = resta > 0

# Mostrar resultado
print("¿La resta es numero positivo?", positivo)