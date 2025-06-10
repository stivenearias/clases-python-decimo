"""
1.	Crear un programa que al ingresar usuario y contraseña, 
valide si son correctos y mostrar Falso o Verdadero. 
El usuario debe ser guardado en una variable como “admin” y 
la contraseña debe ser guardada en otra variable como “admin123”.
"""
# Declarar variables
usuario     = "admin"
contrasena  = "admin123"

# Solicitar el ingreso de usuario y contraseña
usuario_ingresado     = input("Ingrese el usuario: ")
contrasena_ingresada  = input("Ingrese la contraseña: ")

# Validar el usuario y la contraseña
resultado = (usuario_ingresado == usuario) and (contrasena_ingresada == contrasena) 

# Mostrar el resultado
print("El resultado de la validación es:", resultado)