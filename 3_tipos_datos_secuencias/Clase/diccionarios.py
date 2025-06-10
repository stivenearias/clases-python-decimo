# CREAR
persona = {
  "nombre": "Stiven",
  "edad": 25,
  "ciudad": "Medellin"
}

# ACCEDER
print(persona["nombre"])
print(persona["edad"])

# MODIFICAR
persona["edad"] = 23
print(persona)

# AGREGAR
persona["profesion"] = "Ingeniero"
print(persona)

# ELIMINAR
var_nueva = persona.pop("edad")
print(var_nueva)

del persona["ciudad"]
print(persona)

# persona.clear()
print(persona)

# ITERAR
for zzzzz in persona:
  print(zzzzz)

for zzzzz in persona.values():
  print(zzzzz)

for clave, valor in persona.items():
  print(f"{clave}: {valor}.")