# # Cajero automatico con While
# # Permitir que el usuario ingrese su PIN hasta un maximo de 3 intentos.
# # Si el PIN es incorrecto despues de los 3 intentos, se bloquea la cuenta.
# print("\n Cajero automatico con While")

# pin_correcto  = "1234"
# intentos      = 0
# max_intentos  = 3

# while intentos < max_intentos:
#   pin_ingresado = input("Introduce tu PIN: ")
  
#   if pin_ingresado == pin_correcto:
#     print("PIN correcto. Accediendo a tu cuenta...")
#     break
#   else:
#     intentos += 1
#     print(f"PIN incorrecto. Te quedan {max_intentos - intentos} intentos.")
# else:
#   print("Cuenta bloqueada. Demasiados intentos fallidos.")


# Hacer un programa que reciba SOLO numeros enteros y cuando el numero sea
# positivo, dejar de pedir numeros.

# paso 1: declarar contador
numero = -1

# paso 2: Crear logica del while
while numero < 0:
  try:
    numero = int(input("Escribe un numero positivo: "))
    
    if numero < 0:
      print("El numero debe ser positivo. Intenta otra vez.")
  except:
    print("Lo que introduces debe ser un numero entero.")

print("El numero que has introducido es positivo:", numero)