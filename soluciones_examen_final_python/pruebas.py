def contar_voales(texto):
  # Inicializar el contador
  contador_vocales = 0
  # saber las vocales
  vocales = "aeiou"
  # texto este en minusculas
  texto = texto.lower()
  # Hacer un bucle que recorra todos las letras de la cadena
  for letra in texto:
    # Dentor del bucle validar letra por letra si es o no es vocal (condiconales)
    if letra in vocales:
      # Dentor de la condicion hago que se increment eun cntador por cada vocal encontrada
      contador_vocales += 1
  # Retornar la cantidad de vocales
  return contador_vocales

# print(f"Hay {contar_voales("Hola MUNDO")} vcales")

texto = input("Ingrese texto")

print(f"El numeo de vocales es: {contar_voales(texto)}")