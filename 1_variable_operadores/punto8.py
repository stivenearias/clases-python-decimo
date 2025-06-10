"""
Pide al usuario su año de nacimiento y calcula su edad
(asumiendo que el año actual es 2023).
"""
# Asignar variables
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
ano_actual = 2023

# Calcular edad
edad = ano_actual - ano_nacimiento

# Mostrar resultado
print("El usuario tenia", edad, "años en el año 2023")