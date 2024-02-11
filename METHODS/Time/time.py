from datetime import datetime

monthName = { 
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

def getActualTime():
    acTime = datetime.now()

    hour = acTime.hour
    mins = acTime.minute

    if hour > 12:
        hour = abs(hour-12)
        return f'Son las {hour} y {mins} de la tarde'
    elif hour == 12:
        return f'Son las {hour} y {mins} de la tarde'
    else:
        return f'Son las {hour} y {mins} de la mañana'

def getActualDay():
    acTime = datetime.now()

    return f'Hoy es {acTime.day} de {monthName[acTime.month]} de {acTime.year}'