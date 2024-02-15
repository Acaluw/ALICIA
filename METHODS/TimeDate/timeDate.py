#https://pypi.org/project/pytz/
#https://www.youtube.com/watch?v=lUe_-WnrPUE
import pytz
from datetime import datetime
import pycountry
from googletrans import Translator

def traducir_texto(texto, destino='en'):
    translator = Translator()
    # Traducimos el texto al idioma destino
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text 

def obtener_codigo_iso(nombre_pais):
    try:
        # https://pypi.org/project/pycountry/
        # Buscar el país por su nombre con "pycountry" y "search_fuzzy" busca coincidencias aproximadas para manejar posibles errores tipográficos o abreviaturas.
        pais = pycountry.countries.search_fuzzy(nombre_pais)
        # Devolver el código ISO 3166-1 alfa-2 del primer país encontrado
        return pais[0].alpha_2 #type: ignore
    except LookupError:
        return None

def obtener_fecha(frase):
    # Verificamos si la frase contiene palabras clave
    if "fecha" in frase.lower() or "dia es hoy" in frase.lower():
        fecha_actual = datetime.now()
        # Obtenemos el nombre del mes y el día
        nombre_mes = fecha_actual.strftime("%B")
        dia = fecha_actual.strftime("%d")
        # Obtenemos el año
        anio = fecha_actual.strftime("%Y")
        return f"{dia} de {traducir_texto(nombre_mes, 'es')} de {anio}"
    else:
        return False

def obtener_hora(frase):
    # Verificamos si la palabra "hora" está en la frase
    if "hora" in frase.lower():
        # Verificamos si la frase contiene la palabra "en"
        if "en" in frase.lower():
            # Extraemos la ciudad después de la palabra "en", para poder sacar la localización indicada
            nombre_pais = frase.split("en", 1)[1].strip()
            # Traducimos el nombre del pais a Inglés, para que se encuentre en el mismo idioma que en el json
            pais_contexto = "Traduce la siguiente ubicacion: " + nombre_pais
            pais_contexto = traducir_texto(pais_contexto, "en")
            pais_nombre = pais_contexto.split(":", 1)[1].strip()
            # Obtenemos el codigo iso del pais
            codigo_iso = obtener_codigo_iso(pais_nombre)
            if codigo_iso:
                try:
                    # Obtener la zona horaria del país
                    zona_horaria = pytz.country_timezones[codigo_iso.upper()][0]
                    print(zona_horaria)
                    # Obtener la hora actual en esa zona horaria
                    hora_actual = datetime.now(pytz.timezone(zona_horaria))
                    hora_formateada = hora_actual.strftime("%H:%M:%S")
                    mensaje_hora = f"La hora actual en {nombre_pais.capitalize()} es {hora_formateada}"
                    return mensaje_hora
                except KeyError:
                    return "No se encontró información de zona horaria para el país especificado"
            else:
                return "País no encontrado"
        else:
            #Si no se proporciona una ciudad, mostrar la hora local del dispositivo
            hora_local = datetime.now()
            hora_local_formateada = hora_local.strftime("%H:%M:%S")
            mensaje_hora_local = f"La hora actual local es {hora_local_formateada}"
            # Devolvemos el resultado
            return mensaje_hora_local
    else:
        #Si la palabra "hora" no está en la frase, no hacer nada
        return False

frase = input("Introduce una frase: ")
if "fecha" in frase.lower() or "dia es hoy" in frase.lower():
    resultado = obtener_fecha(frase)
    print(resultado)
elif "hora" in frase.lower():
    resultado = obtener_hora(frase)
    print(resultado)
