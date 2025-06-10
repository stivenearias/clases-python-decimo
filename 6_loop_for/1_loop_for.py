# bucle for
# Va a ejecutar un bloque de codigo siempre que un elemento iterable lo permita

animales = ["perro", "gato", "leon", "tigre", "loro", "pez"]

for peluche in animales:
  print(peluche)
  

for i in range(10):
  print(i)
  
# range(inicio, fin, salto)
# range(2, 20, 5)

print("\nrange con inicio, fin y salto")
for i in range(0, 21, 5):
  print(i)
  
print("\nIterar una cade de texto")
palbra = "Python sjdahksdh askdkas"

for letra in palbra:
  print(letra)
  
  
# enummarate()
print("\nFor con enumerate para ver el indice")
animales = ["perro", "gato", "leon", "tigre", "loro", "pez"]

for index, animal in enumerate(animales):
  print(f"{animal} esta en la posicion {index}")
  if index == 4:
    print(f"El animal {animal} esta en la psocion 4")
    

# Como iterar sobre un Diccionario
print("\nIterar con diccionario CLAVE")
frutas = {
  # clave: valor
  "manzana": 1,
  "naranja": 2,
  "banado":   3
}

for clave in frutas:
  print(clave)

print("\nIterar diccionarios con .items()")
for clave, valor in frutas.items():
  print(f"{clave}: {valor}")





