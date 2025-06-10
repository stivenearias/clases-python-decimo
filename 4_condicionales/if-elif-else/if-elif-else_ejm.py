def dia_semana(dia):
    if dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miércoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sábado"
    elif dia == 7:
        return "Domingo"
    else:
        return "Día no válido"
    

# Uso de la función
print(dia_semana(2))  # Imprime "Martes"