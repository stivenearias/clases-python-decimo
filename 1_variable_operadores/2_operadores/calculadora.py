"""
Entrada: dos numeros (num1 y num2)

Salida:
[+] Suma
[-] Resta
[*] Multiplicacion
[/] Divi
[%] Modulo
[**] Potencia
[//] Divi Entera
"""

print("******************************")
print("***** CALCULADORA BASICA *****")
print("******************************")

# Obtener los dos numeros para las operaciones
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

# Proceso para obtener los resultados de las operaciones
suma    = num1 + num2 
resta   = num1 - num2 
multi   = num1 * num2 
divi    = num1 / num2 
modulo  = num1 % num2 
poten   = num1 ** num2 
div_ent = num1 // num2 

print("*********************************************")
print("Los numeros a operar son: ", num1, " y ", num2)
print("*********************************************")

# Mostrar los resultados en pantalla
# print("El resultado de la suma es: ", suma)
# print("El resultado de la resta es: ", resta)
# print("El resultado de la multiplicacion es: ", multi)
# print("El resultado de la division es: ", divi)
# print("El resultado del modulo es: ", modulo)
# print("El resultado de la potencia es: ", poten)
# print("El resultado de la division entera es: ", div_ent)

# Otra forma de imprimir resultados de una forma mas clara
print(f"{num1} + {num2} = {suma}")

print(f"numero 1: {num1} numero 2: {num2}")

print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multi}")
print(f"{num1} / {num2} = {divi}")
print(f"{num1} % {num2} = {modulo}")
print(f"{num1} ** {num2} = {poten}")
print(f"{num1} // {num2} = {div_ent}")