# -*- coding: utf-8 -*-
"""
CALCULADORA DE VIAJE EN AUTOBÚS
-------------------------------
Pasos:
1. Mostrar mensaje de bienvenida.
2. Pedir datos al usuario (distancia, tarifa por km, 
velocidad promedio).
3. Calcular tiempo de viaje y costo total.
4. Mostrar resultados.
"""















# --- PASO 1: Mensaje de bienvenida ---
print("🚍 CALCULADORA DE VIAJE EN AUTOBÚS 🚍")
print("(Ingresa los datos que se te piden)\n")

# --- PASO 2: Pedir datos al usuario ---
distancia = float(input("Distancia del viaje (km): "))
tarifa_por_km = float(input("Tarifa por kilómetro ($): "))
velocidad_promedio = float(input("Velocidad promedio del autobús (km/h): "))

# --- PASO 3: Cálculos ---
tiempo_viaje = distancia / velocidad_promedio  # Tiempo en horas
costo_total = distancia * tarifa_por_km  # Costo en pesos

# --- PASO 4: Mostrar resultados ---
print("\n--- RESULTADOS ---")
print(f"⏱️ Tiempo estimado: {tiempo_viaje:.1f} horas")
print(f"💵 Costo total: ${costo_total:.2f} MXN")
print("\n¡Buen viaje! 😊")