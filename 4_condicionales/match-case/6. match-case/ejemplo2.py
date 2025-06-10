"""
Calculadora MUY BASICA que solo va a sumar y restar 2 numeros
"""

#Pedir la opcion de suma o resta al usuario
operacion = input("¿Que quieres hacer? (sumar o restar): ").lower()

#Pedir los dos numeros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#Vamos a usar el match-case para darle funcion a la calculadora
match operacion:
  case "sumar":
    print(f"La suma es: {num1 + num2}")
  case "sUMar":
    print(f"La suma es: {num1 + num2}")
  case "restar":
    print(f"La resta es: {num1 - num2}")
  case _:
    print("Operacion no valida")