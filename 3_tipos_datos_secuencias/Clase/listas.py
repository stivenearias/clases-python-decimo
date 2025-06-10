# LISTAS
# CREAR
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "mango", "fresa"]

# ACCEDER
print(frutas[1])
print(numeros[4])

# MODIFICAR
numeros[1] = 8
print(numeros)

# AGREGAR
frutas = ["manzana", "mango", "fresa"]
frutas.append("pera")
print(frutas)
frutas.insert(0, "banano")
print(frutas)

# ELIMINAR
frutas.remove("mango")
print(frutas)

elemnto_elimando = frutas.pop()
print(frutas)
print(elemnto_elimando)

del frutas[0]
print(frutas)

# ITERAR
for fruta in frutas:
  print(fruta)