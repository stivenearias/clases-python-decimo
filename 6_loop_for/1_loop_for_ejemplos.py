# Ejemplo 1:
# Iterar sobre una lista y acumular sus valores
numeros = [5, 10, 15, 20]
suma = 0

for num in numeros:
  suma += num
  print(f"Numero actual: {num}")

print(f"La suma es: {suma}")

# Ejemplo 2
# Desarrolar un programa que cuente las vocales en un texto
print("\nEjemplo 2")

texto = "Hola Mundo!"
vocales = 0

for letra in texto:
  if letra.lower() in "aeiou":
    vocales += 1

print(f"Numero de vocales: {vocales}")

# Ejemplo 3
# Encontrar cual es el numero mayor en una lista de numeros
print("\nEjemplo 3")

numeros = [15, 5, 25, 10, 20]
mayor = numeros[0]

for numero in numeros:
  if numero > mayor:
    mayor = numero
    

print(f"El numero mayor de la lista es: {mayor}")