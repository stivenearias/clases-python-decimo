# CREAR
numeros = {1, 2, 3, 4, 5}

#ACCEDER (ITERAR)
for numero in numeros:
  print(numero)

# AGREGAR
numeros.add(6)
print(numeros)

numeros.update([7, 8, 9, 10])
print(numeros)

# ELIMINAR
numeros.remove(10)
print(numeros)

numeros.discard(10)