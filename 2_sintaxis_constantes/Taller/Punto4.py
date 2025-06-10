"""
Estima las emisiones de CO₂ en un 
viaje en tren (gramos por km constante).
"""

CO2_POR_KM = 14  # Gramos de CO₂ por km en tren
distancia = float(input("Distancia del viaje (km): "))
emisiones = distancia * CO2_POR_KM
print(f"🚆 Emites aproximadamente {emisiones} gramos de CO₂.")