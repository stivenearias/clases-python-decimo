# TUPLAS
# Crear
# Ejemplo de una tupla de números
numeros = (1, 2, 3, 4, 5)

# Ejemplo de una tupla de cadenas
frutas = ("manzana", "naranja", "plátano")

# Ejemplo de una tupla mixta
mixta = (1, "Hola", True, 3.14)

# Crear con 1 elemento
# Tupla de un solo elemento
tupla_uno = (42,)

print(type(tupla_uno))  # Imprime: <class 'tuple'>

# Acceder
frutas = ("manzana", "naranja", "plátano")

# Acceder al primer elemento
print(frutas[0])  # Imprime: manzana

# Acceder al último elemento
print(frutas[-1])  # Imprime: plátano

# Iterar
frutas = ("manzana", "naranja", "plátano")

for fruta in frutas:
    print(fruta)