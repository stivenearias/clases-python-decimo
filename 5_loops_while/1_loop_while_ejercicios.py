"""
1. Suma de números hasta '0' (break)
Enunciado:
Pide números al usuario dentro del while.
Si ingresa 0, termina el bucle y muestra la suma acumulada.
"""
suma = 0
while True:
  num = int(input("Ingrese un numero (0 para terminar): "))
  if num == 0: break
  suma += num

print(f"La suma total es: {suma}")

"""
2. Contador hasta límite
Enunciado:
Pide un número límite fuera del while.  
Luego, imprime números del 1 al límite, 
pero omite los múltiplos de 3.
"""
limite = int(input("Ingrese el limite: "))
contador = 1
while contador <= limite:
  if contador % 3 == 0:
    contador += 1
    continue
  print(contador)
  contador += 1

"""
3. Números pares en un rango (while + entrada externa)
Enunciado:
Pide dos números fuera del while (inicio y fin). 
Imprime solo los pares en ese rango usando while.
"""
try:
  inicio  = int(input("Ingrese el numero de inicio: "))
  fin     = int(input("Ingrese el numero de fin: "))

  while inicio <= fin:
    if inicio % 2 == 0:
      print(inicio)
    inicio += 1
except:
  print("Mensaje de error")