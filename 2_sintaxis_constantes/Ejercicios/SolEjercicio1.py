# -*- coding: utf-8 -*-
"""
CALCULADORA DE VIAJE EN AUTO
----------------------------
Pasos:
1. Definir constantes (valores fijos como eficiencia del auto).
2. Pedir datos al usuario (distancia, velocidad, precio gasolina).
3. Calcular tiempo de viaje.
4. Calcular combustible usado.
5. Calcular costo total del viaje.
6. Mostrar resultados con formato claro.
"""

# --- PASO 1: Definir constantes ---
EFICIENCIA = 12  # km por litro (constante para el auto)
HORAS_POR_DIA = 8  # Para calcular paradas si el viaje es muy largo

# --- PASO 2: Pedir datos al usuario ---
distancia = float(input("Distancia del viaje (km): "))
velocidad_promedio = float(input("Velocidad promedio (km/h): "))
precio_gasolina = float(input("Precio de la gasolina por litro: $"))

# --- PASO 3: Calcular tiempo de viaje ---
tiempo_horas = distancia / velocidad_promedio
tiempo_dias = tiempo_horas / HORAS_POR_DIA  # Para viajes largos

# --- PASO 4: Calcular combustible usado ---
litros_usados = distancia / EFICIENCIA

# --- PASO 5: Calcular costo total ---
costo_total = litros_usados * precio_gasolina

# --- PASO 6: Mostrar resultados ---
print("\n--- RESULTADOS ---")
print(f"Tiempo de viaje: {tiempo_horas:.2f} horas ({tiempo_dias:.1f} días con paradas)")
print(f"Combustible necesario: {litros_usados:.1f} litros")
print(f"Costo estimado: ${costo_total:.2f}")

# --- Extras: Validación básica ---
if litros_usados > 50:
    print("\n¡Advertencia! Necesitarás un tanque adicional.")