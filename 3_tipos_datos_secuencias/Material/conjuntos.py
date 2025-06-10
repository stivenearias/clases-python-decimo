# CONJUNTOS
# Crear
# Crear un conjunto con llaves
conjunto = {1, 2, 3, 4, 5}

# Crear un conjunto usando la función set()
conjunto_vacio = set()

# Crear un conjunto con elementos repetidos
conjunto_sin_duplicados = {1, 2, 2, 3, 4}

print(conjunto_sin_duplicados)  # Imprime: {1, 2, 3, 4}

# Acceder (Iterando)
conjunto = {"manzana", "naranja", "plátano"}

for fruta in conjunto:
    print(fruta)

# Agregar
conjunto = {1, 2, 3}

# Agregar un nuevo elemento
conjunto.add(4)

print(conjunto)  # Imprime: {1, 2, 3, 4}

# Agregar múltiples elementos
conjunto.update([5, 6])

print(conjunto)  # Imprime: {1, 2, 3, 4, 5, 6}

# Eliminar
conjunto = {0, 1, 2, 3, 4}

# Eliminar un elemento
conjunto.remove(2)

print(conjunto)  # Imprime: {1, 3, 4}

# Eliminar un elemento (sin error si no existe)
conjunto.discard(5)

print(conjunto)  # Imprime: {1, 3, 4} (sin errores)

# Eliminar un elemento arbitrario
elemento = conjunto.pop()

print(elemento)  # Imprime uno de los elementos eliminados
print(conjunto)  # Imprime el conjunto restante