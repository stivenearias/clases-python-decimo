"""
CALCULA EL PRECIO FINAL DE UN PRODUCTO INGRESADO POR ELUSUARIO APLICANDO UN IVA DEL 19%.
"""

IVA = 0.16  # 16%
precio_sin_iva = 200
precio_con_iva = precio_sin_iva * (1 + IVA)
print("Precio final:", precio_con_iva)  # Salida: 232.0