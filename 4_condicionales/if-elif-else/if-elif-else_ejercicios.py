# Verificar si un numero es positivo

# Dispositivo de temperatura
# temperatura = int(input("Ingrese temperatura:"))

# if temperatura > 40:
#   print("Alerta: Temperatura alta!")

  # Acceso a juego: Si el usuario ingresa la contraseña "pass123"
  # imprimir un mensaje que diga "Acceso concedido"

#EJEMPLOS CON if-else
#Número par o impar: Pide un número al usuario y 
# determina si es par o impar. Imprime el resultado.
numero = int(input("Ingrese un numero"))

if numero % 2 == 0:
  print("Es par")
else:
  print("Es impar")

"""
Simula un radar: si la velocidad del auto es mayor a 100 km/h, 
imprime "Multa por exceso de velocidad"; 
de lo contrario, "Velocidad permitida".
"""

"""
lunes -> Inicio de semana
viernes -> ¡Por fin viernes!
Domingo -> Fin de semana
-> Dia no reconocido
"""
dia = "lunes"

if dia == "lunes":
  print("Inicio de semana")
elif dia == "viernes":
  print("¡Por fin viernes!")


"""
Pide la edad del usuario y clasifícala:

Menor de 13: "Niño"
13 a 19: "Adolescente"
20 a 64: "Adulto"
65 o más: "Adulto mayor"
"""

"""
Pide al usuario ingresar el clima actual 
("soleado", "lluvioso", "nublado").

Según la opción, sugiere una acción:
"soleado": "Lleva protector solar"
"lluvioso": "Lleva paraguas"
"nublado": "Puedes salir sin problemas"
Otro caso: "Clima no reconocido"
"""