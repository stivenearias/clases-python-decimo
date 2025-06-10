# Hacer que un numero coincida con su patron numerico

numero = 2

match numero:
  case 1:
    # Codigo
    print("Es uno.")
  case 2:
    print("Es dos.")
  case 3:
    print("Es tres.")
  case _:
    print("Numero desconocido")

dia = "Lunes"
dia.lower()

match dia:
  case "lunes":
    print("Esta en semana")
  case "martes":
    print("Esta en semana")
  case "miercoles":
    print("Esta en semana")
  case "sabado":
    print("Esta en fin de semana")
  case 123:
    print("Son numeros")
  case _:
    print("El dia es desconocido")




