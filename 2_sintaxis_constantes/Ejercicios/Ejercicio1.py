"""
CALCULADORA DE VIAJE EN AUTO
----------------------------
Pasos:
1. Definir constantes (valores fijos como eficiencia del auto).
2. Pedir datos al usuario (distancia, velocidad, precio gasolina).
3. Calcular tiempo de viaje.
4. Calcular combustible usado. D/E
5. Calcular costo total del viaje. LU*PG
6. Mostrar resultados con formato claro.
"""

#Paso 1: Definir constantes
EFICIENCIA   = 22 # Km recoridos por listro de gasolina
HORA_POR_DIA = 8  # Paradas si el viaje es muy largo

# Paso 2: Pedir datos al usuario
distancia         = float(input("Ingrese la distancia recorrida: "))
velociad_promedio = float(input("Ingrese la velocidad promedio: "))
precio_gasolina   = float(input("Ingrese el precio de la gasolina: "))

# Paso 3: Calcular tiempo de viaje
tiempo_horas = distancia / velociad_promedio
tiempo_dias  = tiempo_horas / HORA_POR_DIA

# Paso 4: Calcular combustible usado
combustible_usado = distancia / EFICIENCIA

# Paso 5: Calcular el costo total del viaje
costo_total = combustible_usado * precio_gasolina

# Paso 6: Mostrar los resultados
print(f"El tiempo recorrido en horas fue de: {tiempo_horas} y en dias: {tiempo_dias}") # Mostrar el tiempo recorido
print(f"El comustible usado en el viejae fue de: {combustible_usado:.2f}") # Mostrar combustible usado
print(f"El costo total del viaje fue de: {costo_total}") # Mostrar costo toal del viaje

if distancia > 100:
  print("Recurda tanquear.")