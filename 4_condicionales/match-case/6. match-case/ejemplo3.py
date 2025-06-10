"""
Pedirle al usuario que ingrese su edad.
Mostrar un mensaje si:
  (0-12) Niño
  (13-17) Adolecente
  (18-64) Adulto
  (65 en adelante) Adulto Mayor
"""

# Pedir edad
edad = int(input("Ingrese su edad: "))

match edad:
  case edad if 0 <= edad <= 12:
    print("Eres un niño.")
  case edad if 13 <= edad <= 17:
    print("Eres adulto.")
  case edad if 18 <= edad <= 64:
    print("Eres mayor.")
  case edad if edad >= 65:
    print("Eres adulto mayor.")
  case _:
    print("Edad no valida.")