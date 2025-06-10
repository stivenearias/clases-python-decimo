# DICCIONARIOS
# Crear
# Crear un diccionario de ejemplo
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Lima"
}

# Crear un diccionario vacío
diccionario_vacio = {}

# Acceder
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Lima"
}

# Acceder al valor de la clave "nombre"
print(persona["nombre"])  # Imprime: Carlos

# Modificar
# Modificar el valor de una clave existente
persona["edad"] = 31

print(persona)  # Imprime: {'nombre': 'Carlos', 'edad': 31, 'ciudad': 'Lima'}

# Agregar
# Agregar un nuevo par clave-valor
persona["profesion"] = "Ingeniero"

print(persona)  # Imprime: {'nombre': 'Carlos', 'edad': 31, 'ciudad': 'Lima', 'profesion': 'Ingeniero'}

# Eliminar
# Eliminar un elemento por su clave
edad = persona.pop("edad")

print(edad)  # Imprime: 31
print(persona)  # Imprime: {'nombre': 'Carlos', 'ciudad': 'Lima', 'profesion': 'Ingeniero'}

# Eliminar un elemento
del persona["ciudad"]

print(persona)  # Imprime: {'nombre': 'Carlos', 'profesion': 'Ingeniero'}

# Eliminar todos los elementos
persona.clear()

print(persona)  # Imprime: {}

# Iterar
#Iterar Sobre las Claves
for clave in persona:
  print(clave)

#Iterar Sobre los Valores
for valor in persona.values():
    print(valor)

#Iterar Sobre Claves y Valores
for clave, valor in persona.items():
  print(f"{clave}: {valor}")
  