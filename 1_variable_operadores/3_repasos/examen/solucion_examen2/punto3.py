"""
3.	Crear un programa que pida el nombre de un usuario, 
su edad y ciudad donde vive, debe mostrar el nombre del usuario 
y decir si es mayor de edad con un mensaje que 
respete la siguiente estructura: 
“El usuario NOMBRE tiene EDAD años y vive en CIUDAD.
"""

# Declarar y pedir las variables
nombre  = input("Ingrese el nombre del usuario: ")
edad    = int(input("Ingrese la edad del usuario: "))
ciudad  = input("Ingrese la ciudad donde vive el usuario: ")

# Calcular si es mayor de edad
mayor_edad = edad >= 18

# Mostrar los resultados
# f-strings
print(f"El usuario {nombre} tiene {edad} años y vive en {ciudad}.")
print("¿El usuario es mayor de edad?:", mayor_edad)