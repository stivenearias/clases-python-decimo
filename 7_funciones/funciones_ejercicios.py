"""
Ejercicio 1: Calcular la media de una lista
Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
Calcula la media de los números usando un bucle for.
"""
numeros_lista = [10, 20, 30, 40, 50]

def calc_media(numeros):
  suma = 0 
  for num in numeros:
    suma += num
  media = suma / len(numeros)
  return media

respuesta = calc_media(numeros_lista)
print(respuesta)
# """
# Ejercicio 2: Tabla de multiplicar
# Pidele al usuario que ingrese un numero.
# Vas a mostrar la tabla de multiplicar de ese numero del 1 al 10 usando el bucle for.
# """
# # Le dipes el numero
# numero = int(input("Ingrese el numero del que quiere la tabla de multiplicar: "))
# for i in range(1, 11):
#   print(f"{numero} x {i} = {numero * i}")
# """
# Ejercicio 3: Encontrar el número mayor y menor en una lista
# Dada la siguiente lista de numeros:
# numeros = [23, 5, 67, 12, 98, 3]
# Encuentre el numero mayor y menor en la lista con for.
# """