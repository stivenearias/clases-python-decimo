# LISTAS
# Crear
# Ejemplo de una lista de números
numeros = [1, 2, 3, 4, 5]

# Ejemplo de una lista de cadenas
frutas = ["manzana", "naranja", "plátano"]

# Ejemplo de una lista mixta
mixta = [1, "Hola", True, 3.14]

# Acceder
frutas = ["manzana", "naranja", "plátano"]

# Acceder al primer elemento
print(frutas[0])  # Imprime: manzana

# Acceder al segundo elemento
print(frutas[1])  # Imprime: naranja

# Modificar
numeros = [1, 2, 3, 4, 5]

# Cambiar el tercer elemento
numeros[2] = 10

print(numeros)  # Imprime: [1, 2, 10, 4, 5]

# Agregar
frutas = ["manzana", "naranja"]

# Agregar un elemento al final de la lista
frutas.append("plátano")

print(frutas)  # Imprime: ['manzana', 'naranja', 'plátano']

# Insertar un elemento en la segunda posición
frutas.insert(1, "pera")

print(frutas)  # Imprime: ['manzana', 'pera', 'naranja', 'plátano']

# Eliminar
# Eliminar "naranja" de la lista
frutas.remove("naranja")

print(frutas)  # Imprime: ['manzana', 'plátano']

# Eliminar el último elemento
fruta = frutas.pop()

print(frutas)  # Imprime: ['manzana']
print(fruta)  # Imprime: plátano

# Eliminar el primer elemento
del frutas[0]

print(frutas)  # Imprime: []

# Iterar
frutas = ["manzana", "naranja", "plátano"]

for fruta in frutas:
    print(fruta)