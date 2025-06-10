def dia_semana(dia):
  match dia:
    case 1:
        return "Lunes"
    case 2:
        return "Martes"
    case 3:
        return "Miércoles"
    case 4:
        return "Jueves"
    case 5:
        return "Viernes"
    case 6:
        return "Sábado"
    case 7:
        return "Domingo"
    case _:
        return "Día no válido"

# Uso de la función
print(dia_semana(4))  # Imprime "Jueves"