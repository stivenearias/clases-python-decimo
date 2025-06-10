"""
Ejercicio 2: Diccionario de Contactos

Crea un programa que simule una agenda de contactos usando un diccionario:

1. El programa debe permitir al usuario (una funcion para cada acción):
  - Agregar un contacto (nombre y teléfono).
  - Buscar un contacto por nombre.
  - Mostrar todos los contactos.

2. Usa un bucle while para que el menú se repita hasta que el usuario elija Salir.

3. Implementa funciones separadas para cada opción (agregar, buscar, mostrar).

4. Usa match-case (o if-elif-else) para manejar las opciones del menú.
"""

def agregar_contacto(agenda):
  """Agrega un nuevo contacto a la agenda."""
  nombre = input("Ingrese el nombre del contacto: ").strip()
  telefono = input("Ingrese el teléfono del contacto: ").strip()
  
  if nombre and telefono:  # Verifica que no estén vacíos
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado exitosamente.")
  else:
    print("Error: Nombre y teléfono no pueden estar vacíos.")

def buscar_contacto(agenda):
  """Busca un contacto por nombre y muestra su teléfono."""
  nombre = input("Ingrese el nombre a buscar: ").strip()
  if nombre in agenda:
    print(f"Teléfono de {nombre}: {agenda[nombre]}")
  else:
    print(f"Contacto '{nombre}' no encontrado.")

def mostrar_contactos(agenda):
  """Muestra todos los contactos en la agenda."""
  if not agenda:  # Si el diccionario está vacío
    print("La agenda está vacía.")
  else:
    print("\n--- Lista de Contactos ---")
    for nombre, telefono in agenda.items():
      print(f"{nombre}: {telefono}")

def main():
  """Función principal que maneja el menú interactivo."""
  agenda = {}  # Diccionario para almacenar los contactos
  
  while True:
    print("\n--- Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ").strip()
    
    match opcion:  # Usamos match-case (Python 3.10+)
      case "1":
        agregar_contacto(agenda)
      case "2":
        buscar_contacto(agenda)
      case "3":
        mostrar_contactos(agenda)
      case "4":
        print("Saliendo del programa...")
        break
      case _:
        print("Opción inválida. Intente nuevamente.")

main()