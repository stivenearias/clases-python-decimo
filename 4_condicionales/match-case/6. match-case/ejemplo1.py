"""
Vamos a tener 3 opciones:
1. Evaluar si un numero es positivo o negativo y mostrar el mensaje
2. Pedir 2 numeros al usuario y los vamos a sumar
3. Pedir un dia de la semana y si ingresa sabado que muestre "es hora de descasar"
Si no ingresa una opcion correcta, vamos a pedir el nombre del usuario y le vamos a mostrar un
mensaje donde le pedimos que ingrese una opcion correcta.
"""

# Dando contexto al usuario de lo que va a hacer
print("Marque una opcion segun lo que necesite:")
print("1. Evaluar")
print("2. Sumar dos numeros")
print("3. Dia de la semna")

# Pedirle al usuario la opcion
opcion = int(input("Ingrese una opcion: "))

# Ejecutar el codigo segun la opcion ingresada por el usuario
match opcion:
  case 1:
    # Codigo que se ejecuta cuando la opcion es 1
    num = float(input("Ingrese un numero: "))
    
    if num > 0:
      print("Es positivo")
    elif num == 0:
      print("Es neutro")
    else:
      print("Es negativo")
  case 2:
    num1 = int(input("Ingrese numero 1: "))
    num2 = int(input("Ingrese numero 2: "))
    
    suma = num1 + num2
    
    print(f"La suma de {num1} y {num2} es {suma}")
  case 3:
    #Pedir dia de la semana
    dia = input("ingrese un dia de la semana: ")
    
    if dia == "sabado":
      print("es hora de descasar")
    else:
      print("Dia desconocido")
  case _:
    nombre = input("Ingrese su nombre: ")
    
    print("Hola, ", nombre, ". Por favor ingrese una opcion valida.")