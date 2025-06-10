"""
Aplica un descuento del 10% (constante) 
a un precio ingresado por el usuario.
"""

DESCUENTO = 0.10  # 10%
precio_original = float(input("Ingresa el precio: "))
precio_con_descuento = precio_original * (1 - DESCUENTO)
print("Precio con descuento:", precio_con_descuento)