
# Bucle while simple
print("\n Bucle while simple")

# num
num = 0
# string
str = ""
# listas
list = []
# diccionarios
dic = {}

contador = 0
while contador <= 5:
  print(contador)
  contador += 1
  
print("\n Bucle while con break")
contador = 0

while contador <= 10:
  print(contador)
  if contador == 5:
    break # Detiene el bucle cuando el contador es 5
  contador += 1
  
print("\n Bucle while con continue")
contador = 0

while contador <= 10:
  contador += 1
  if contador % 2 == 0:
    continue # Va a saltar la iteraccion donde el contador es par
  # 👇🏽 No se va a ejecutar
  print(contador)

# Detectar que la contraseña sea correcta
intento = ""

while intento != "pass1234":
  intento = input("Introduce la contraseña: ")

print("Contraseña es correcta")

print("\n Bucle while con else")
contador = 1

while contador <= 3:
  print(contador)
  if contador == 2:
    break
  contador += 1
else:
  print("El bucle ha terminado correctamente.")