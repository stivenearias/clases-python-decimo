# ]Funciones
# Son un bloque de codigo que se ejecuta cuando se llama y que se puede reutilizar.
# QUe podemos hacer con las funciones:
# Pasarle datos (argumentos)
# Podemos devolver un valor como resultado (opcinal)

# Estructura o sintaxis
"""
def nombre_de_la_funcion(parametro1, parametro2, parametro3, ...)
  #docstring (la documentacion de la funcion)
  #cuerpo de la funcion
  return valor # opcional
"""

print("\nFuncion simple")
def saludar():
  """Esta funcion va a decir Hola"""
  print("Hola")

# Llamamos la funcion
saludar()

print("\nFuncion con paramtros")
def saludar_a(nombre):
  print(f"Hola, {nombre}")
  

saludar_a("Salomes")

saludar_a("Stiven")
saludar_a("Julian")

print("\nFuncion con mmas de un paramtro o multiples paramtros")
def sumar(a, b):
  # print(f"{a + b}")
  return a + b

resultado = sumar(2, 3)
print(resultado)

print("\nFuncion con parametros por defecto")
def saludar_con_parametro(nombre = "Mundo"):
  print(f"Hola, {nombre}")
  

saludar_con_parametro()
saludar_con_parametro("Diego")

print("\nFuncion que retorna multiples valores")
def operaciones(num1, num2):
  suma = num1 + num2
  resta = num1 - num2
  return suma, resta

# Almacenar los valores retornados en dos variables
resultado_suma, resultdo_resta = operaciones(5, 3)
print(f"Suma: {resultado_suma} y la resta: {resultdo_resta}")

# Ejemplo 1
def infromacion_personal(nombre, edad, sexo):
  print(f"{nombre} tiene {edad} y es {sexo}")
  

infromacion_personal("Stiven", 25, "Hombre")
infromacion_personal(edad = 25, sexo = "Hombre",nombre = "Stiven")