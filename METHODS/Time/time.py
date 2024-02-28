#https://pypi.org/project/pytz/
#https://www.youtube.com/watch?v=lUe_-WnrPUE

from datetime import datetime
import pytz
import pycountry
from googletrans import Translator

monthName = { 
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

# translateText(text: string, d: string) -> Translate given text value
def translateText(text, d='en'):
    translator = Translator()
    # Translate the text to the language we want
    res = translator.translate(text, dest=d)
    return res.text 

# getIsoCode(country: string) -> Gets isoCode from the country's value
def getIsoCode(country):
    try:
        # https://pypi.org/project/pycountry/
        # Search for the country by its name with "pycountry", and "search_fuzzy" looks 
        # for approximate matches to handle possible typos or abbreviations.
        pais = pycountry.countries.search_fuzzy(country)
        # Return the ISO 3166-1 alpha-2 code of the first found country
        return pais[0].alpha_2 #type: ignore
    except LookupError:
        return None

# getHour(input: string) -> Gets hour from the input's value place
def getHour(input): 
    # Check if the word "hora" is in the sentence
    if "hora" in input.lower():
        # Check if the sentence contains the word "en"
        if "en" in input.lower():
            # Extract the city after the word "en", to be able to achieve the indicated location
            nombre_pais = input.split("en", 1)[1].strip()
            # Translate the country name to English, so it is in the same language as in the JSON
            pais_contexto = "Traduce la siguiente ubicacion: " + nombre_pais
            pais_contexto = translateText(pais_contexto, "en")
            pais_nombre = pais_contexto.split(":", 1)[1].strip()
            # Get the ISO code of the country
            codigo_iso = getIsoCode(pais_nombre)
            if codigo_iso:
                try:
                    # Get the time zone of the country
                    zona_horaria = pytz.country_timezones[codigo_iso.upper()][0]
                    print(zona_horaria)
                    # Get the current time in that time zone
                    hora_actual = datetime.now(pytz.timezone(zona_horaria))
                    # Format the time
                    hora_formateada = hora_actual.strftime("%H:%M:%S")
                    mensaje_hora = f"La hora actual en {nombre_pais.capitalize()} es {hora_formateada}"
                    return mensaje_hora
                except KeyError:
                    return "No se encontró información de zona horaria para el país especificado"
            else:
                return "País no encontrado"
    else:
        # If the word "hora" is not in the sentence, do nothing
        return False

# getActualTime() -> Gets actual time
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

# getActualDay() -> Gets actual day
def getActualDay():
    acTime = datetime.now()

    return f'Hoy es {acTime.day} de {monthName[acTime.month]} de {acTime.year}'