#https://pypi.org/project/pytz/
#https://www.youtube.com/watch?v=lUe_-WnrPUE
# Importing libraries
import pytz
from datetime import datetime
import pycountry
from googletrans import Translator

def traducir_texto(texto, destino='en'):
    translator = Translator()
    # Translate the text to the language we want
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text 

def obtener_codigo_iso(nombre_pais):
    try:
        # https://pypi.org/project/pycountry/
        # Search for the country by its name with "pycountry", and "search_fuzzy" looks 
        # for approximate matches to handle possible typos or abbreviations.
        pais = pycountry.countries.search_fuzzy(nombre_pais)
        # Return the ISO 3166-1 alpha-2 code of the first found country
        return pais[0].alpha_2 #type: ignore
    except LookupError:
        return None

def obtener_fecha(frase):
    # Check if the sentence contains keywords
    if "fecha" in frase.lower() or "dia es hoy" in frase.lower():
        fecha_actual = datetime.now()
        # Get the name of the month and the day
        nombre_mes = fecha_actual.strftime("%B")
        dia = fecha_actual.strftime("%d")
        # Get the year
        anio = fecha_actual.strftime("%Y")
        return f"{dia} de {traducir_texto(nombre_mes, 'es')} de {anio}"
    else:
        return False

def obtener_hora(frase): 
    # Check if the word "hora" is in the sentence
    if "hora" in frase.lower():
        # Check if the sentence contains the word "en"
        if "en" in frase.lower():
            # Extract the city after the word "en", to be able to achieve the indicated location
            nombre_pais = frase.split("en", 1)[1].strip()
            # Translate the country name to English, so it is in the same language as in the JSON
            pais_contexto = "Traduce la siguiente ubicacion: " + nombre_pais
            pais_contexto = traducir_texto(pais_contexto, "en")
            pais_nombre = pais_contexto.split(":", 1)[1].strip()
            # Get the ISO code of the country
            codigo_iso = obtener_codigo_iso(pais_nombre)
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
            # If no city is provided, show the local time of the device, "local time"
            hora_local = datetime.now()
            # Format the time
            hora_local_formateada = hora_local.strftime("%H:%M:%S")
            mensaje_hora_local = f"La hora actual local es {hora_local_formateada}"
            return mensaje_hora_local
    else:
        # If the word "hora" is not in the sentence, do nothing
        return False
    
"""
if __name__ == '__main__':
    peticion_busqueda = input("De que país quieres saber la hora: ")
    obtener_capital(peticion_busqueda)"""

frase = input("Introduce una frase: ")
if "fecha" in frase.lower() or "dia es hoy" in frase.lower():
    resultado = obtener_fecha(frase)
    print(resultado)
elif "hora" in frase.lower():
    resultado = obtener_hora(frase)
    print(resultado)
