# Match para ingresar el numeral de ejercicio a aplicar

print("Ingrese el numero del ejercicio que desea aplicar:")
print("1. Validar usuario y contraseña.")
print("2. Operaciones cun 3 numeros.")
print("3. Pedir datos de usuairo y mostrarlos.")
print("4. Area de una esfera y validación.")
print("5. Calculos con 2 numeros.")
print("6. Salir del programa.")


option = int(input("Ingrese el número del ejercicio a aplicar (1-5): "))

match option:
  case 1:
    """
    1.	Crear un programa que al ingresar usuario y contraseña, 
    valide si son correctos y mostrar Falso o Verdadero.
    El usuario debe ser guardado en una variable como “admin” y 
    la contraseña debe ser guardada en otra variable como “admin123”.
    """
    correct_user = "admin"
    correct_password = "admin123"
    user = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    is_valid = (user == correct_user) and (password == correct_password)
    print("¿Usuario y contraseña válidos?", is_valid)
  case 2:
    """
    2.	Crear un programa que ingresados 3 numeros haga lo siguiente:
      a.	Sumar el numero 1 con el numero 2 y decir si es multiplo de 2
      b.	Mostrar el promedio de los 3 numeros
      c.	Restar el numero 2 con el numero 3 y decir si es un numero positivo
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    # Sumar el numero 1 con el numero 2 y decir si es multiplo de 2
    suma = num1 + num2
    es_multiplo_de_2 = (suma % 2 == 0)
    print(f"La suma de {num1} y {num2} es {suma}. ¿Es múltiplo de 2? {es_multiplo_de_2}")

    # Mostrar el promedio de los 3 numeros
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio de los tres números es: {promedio}")

    # Restar el numero 2 con el numero 3 y decir si es un numero positivo
    resta = num2 - num3
    es_positivo = (resta > 0)
    print(f"La resta de {num2} y {num3} es {resta}. ¿Es positivo? {es_positivo}")
  case 3:
    """
    3.	Crear un programa que pida el nombre de un usuario, su edad y
    ciudad donde vive, debe mostrar el nombre del usuario y decir 
    si es mayor de edad con un mensaje que respete la siguiente estructura: 
    “El usuario Stiven tiene 25 años y vive en Medellín”.
    """
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese la ciudad donde vive: ")

    es_mayor_de_edad = (edad >= 18)
    print(f"El usuario {nombre} tiene {edad} años y vive en {ciudad}. ¿Es mayor de edad? {es_mayor_de_edad}")
  case 4:
    """
    4.	Crear un programa que reciba el radio de una esfera y 
    con este calcular el área de la esfera, mostrar el valor del área y 
    decir si ese valor es mayor a 100.
    """
    radio = float(input("Ingrese el radio de la esfera: "))
    area = 4 * 3.1416 * (radio ** 2)
    es_mayor_a_100 = (area > 100)

    print(f"El área de la esfera es: {area}. ¿Es mayor a 100? {es_mayor_a_100}")
  case 5:
    """
    5.	Crear un programa que reciba dos números y decir 
    si el numero 1 es menor al numero 2 y 
    si numero 2 es diferente de 0.
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    calculo1 = (num1 < num2)
    calculo2 = (num2 != 0)
    print(f"¿El número 1 ({num1}) es menor al número 2 ({num2}) y número 2 es diferente de 0? {calculo1 and calculo2}")
  case 6:
    # Salir del programa.
    
    print("Saliendo del programa...")
    exit()
  case _:
    print("Opción no válida. Por favor, elija un número del 1 al 6.")