"""
Ejercicio 1: Analizador de Texto

Crea un programa que:

1. Pida al usuario ingresar un texto (frase o párrafo).

2. Con funciones, calcule y muestre lo siguiente:
  - Número de vocales (a, e, i, o, u) en el texto (usar for y condicionales).
  - Número de palabras (separadas por espacios).
  - Determinar si el texto es largo o corto:
    "Corto" si tiene menos de 10 caracteres.
    "Mediano" si tiene entre 10 y 30 caracteres.
    "Largo" si tiene más de 30 caracteres (usar len() y condicionales).

3. Imprimir todos los resultados con formatos claros (ej: "Vocales: 5").

"""

"""
Requisitos adicionales:
  - Usa un bucle para permitir que el usuario analice otro texto 
  sin salir del programa (hasta que ingrese "salir").
  - Maneja mayúsculas/minúsculas (ej: contar 'A' como vocal).
  - Usar funciones para cada tarea requerida
"""












def contar_vocales(texto):
  """Cuenta las vocales (a, e, i, o, u) en un texto, ignorando mayúsculas/minúsculas."""
  vocales = "aeiou"
  texto = texto.lower()  # Convertir a minúsculas para simplificar
  contador = 0
  for letra in texto:
    if letra in vocales:
      contador += 1
  return contador

def contar_palabras(texto):
  """Cuenta las palabras en un texto (separadas por espacios)."""
  palabras = texto.split()  # Divide el texto en palabras
  return len(palabras)

def clasificar_longitud(texto):
  """Clasifica el texto como Corto, Mediano o Largo según su longitud."""
  longitud = len(texto)
  if longitud < 10:
    return "Corto"
  elif 10 <= longitud <= 30:
    return "Mediano"
  else:
    return "Largo"

def main():
  """Función principal que maneja el bucle y la interacción con el usuario."""
  while True:
    print("\n--- Analizador de Texto ---")
    texto = input("Ingresa un texto (o escribe 'salir' para terminar): ").strip()
    
    if texto.lower() == "salir":
      print("¡Hasta luego!")
      break
    
    if not texto:  # Si el texto está vacío
      print("Error: No ingresaste nada.")
      continue
    
    # Llamar a las funciones y mostrar resultados
    print("\nResultados:")
    print(f"- Vocales: {contar_vocales(texto)}")
    print(f"- Palabras: {contar_palabras(texto)}")
    print(f"- Longitud: {clasificar_longitud(texto)}")

main()

"""
Recuerden:
1. Comentar las funciones
2. El uso del lower() donde sea necesario
3. Comentar lo que van haciendo para una buena comprension del codigo
4. El uso del try except
"""