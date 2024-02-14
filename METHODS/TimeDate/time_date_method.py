# Importar librerias
# https://geopy.readthedocs.io/en/stable/
from geopy.geocoders import Nominatim
from datetime import datetime
# https://pypi.org/project/timezonefinder/3.4.2/
from timezonefinder import TimezoneFinder
import pytz
from googletrans import Translator
from geopy.geocoders import Nominatim

def obtener_hora(frase):
    # Verificamos si la palabra "hora" está en la frase
    if "hora" in frase.lower():
        # Creamos un objeto Nominatim para poder obtener las coordenadasa geográficas a partir de una ubicación
        geolocator = Nominatim(user_agent = "obtener_hora_AliceAI")
        # Verificamos si la frase contiene la palabra "en"
        if "en" in frase.lower():
            # Extraemos la ciudad después de la palabra "en", para poder sacar la localización indicada
            ciudad = frase.split("en", 1)[1].strip()
            # Obtenemos las coordenadas de la localización
            location = geolocator.geocode(ciudad)
            # Comprobamos si es una localización válida
            if location:
                # Creamos el objeto de la clase TimezoneFinder
                tf = TimezoneFinder()
                # TimezoneFinder se utiliza para encontrar la zona horaria asociada con unas coordenadas geográficas específicas.
                # Obtenemos la zona horaria de las coordenadas
                zona_horaria = tf.timezone_at(lng = location.longitude, lat = location.latitude) #type: ignore
                # Obtenemos con el objeto datetime la hora actual en la zona horaria especificada
                hora_actual = datetime.now(pytz.timezone(zona_horaria)) #type: ignore
                # Formateamos la hora: horas, minutos, segundos
                hora_formateada = hora_actual.strftime("%H:%M:%S")
                # Devolvemos el resultado
                return f"La hora actual en {ciudad.capitalize()} es {hora_formateada}"
        else:
            #Si no se proporciona una ciudad, mostrar la hora local del dispositivo
            hora_local = datetime.now()
            hora_local_formateada = hora_local.strftime("%H:%M:%S")
            # Devolvemos el resultado
            return f"La hora actual local es {hora_local_formateada}"
    else:
        #Si la palabra "hora" no está en la frase, no hacer nada
        return False

def traducir_texto(texto, destino='en'):
    translator = Translator()
    # Traducimos el texto al idioma destino
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text 

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

frase = input("Introduce una frase: ")
if "fecha" in frase.lower() or "dia es hoy" in frase.lower():
    resultado = obtener_fecha(frase)
    print(resultado)
elif "hora" in frase.lower():
    resultado = obtener_hora(frase)
    print(resultado)
