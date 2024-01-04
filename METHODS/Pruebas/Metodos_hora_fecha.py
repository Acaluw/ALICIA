from geopy.geocoders import Nominatim
from datetime import datetime
from timezonefinder import TimezoneFinder
import pytz

def obtener_hora(frase):
    #Verificar si la palabra "hora" está en la frase
    if "hora" in frase.lower():
        geolocator = Nominatim(user_agent="obtener_hora_app")

        #Verificar si la frase contiene la palabra "en"
        if "en" in frase.lower():
            #Extraer la ciudad después de la palabra "en"
            ciudad = frase.split("en", 1)[1].strip()
            location = geolocator.geocode(ciudad)
            if location:
                #Obtener la zona horaria de las coordenadas
                tf = TimezoneFinder()
                zona_horaria = tf.timezone_at(lng=location.longitude, lat=location.latitude)

                #Obtener la hora actual en la zona horaria especificada
                hora_actual = datetime.now(pytz.timezone(zona_horaria))

                #Formatear la hora
                hora_formateada = hora_actual.strftime("%H:%M:%S")

                return f"La hora actual en {ciudad.capitalize()} es {hora_formateada}"
        else:
            #Si no se proporciona una ciudad, mostrar la hora local
            hora_local = datetime.now()
            hora_local_formateada = hora_local.strftime("%H:%M:%S")

            return f"La hora actual local es {hora_local_formateada}"
    else:
        #Si la palabra "hora" no está en la frase, no hacer nada
        return False

from googletrans import Translator
import requests
from geopy.geocoders import Nominatim

def kelvin_a_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def traducir_texto(texto, destino='en'):
    translator = Translator()
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text

def obtener_pais_local():
    try:
        # Obtener la dirección IP del usuario
        ip_info = requests.get('https://ipinfo.io/json')
        ip_data = ip_info.json()

        # Obtener las siglas del país desde la información de la IP
        codigo_pais = ip_data.get('country', 'Desconocido')

        # Obtener el nombre completo del país utilizando geolocalización inversa
        url_geolocalizacion = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={ip_data["loc"].split(",")[0]}&lon={ip_data["loc"].split(",")[1]}'
        respuesta_geolocalizacion = requests.get(url_geolocalizacion)
        datos_geolocalizacion = respuesta_geolocalizacion.json()
        nombre_pais = datos_geolocalizacion.get('address', {}).get('country', 'Desconocido')

        return nombre_pais
    except Exception as e:
        print(f"Error al obtener la información de la IP: {e}")
        return 'Desconocido'

def obtener_clima(frase):
    if "tiempo" in frase.lower() or "clima" in frase.lower():
        #Usamos esto para saber si el un pais o ciudad real
        geolocator = Nominatim(user_agent="obtener_clima_app")
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "ee8c71bbe4bdc1dfea0d3611a656c853"

        if "en" in frase.lower():
            ciudad = frase.split("en", 1)[1].strip()
            #Aqui comprobamos si existe el lugar
            location = geolocator.geocode(ciudad)
            if location:
                url = f"{BASE_URL}appid={API_KEY}&q={ciudad}"
                datos_clima = requests.get(url).json()

                if 'main' in datos_clima and 'weather' in datos_clima:
                    temp_kelvin = datos_clima['main']['temp']
                    temp_celsius = kelvin_a_celsius(temp_kelvin)
                    humedad = datos_clima['main']['humidity']
                    descripcion = datos_clima['weather'][0]['description']

                    idioma_destino = "es"
                    mensaje_clima = f'El clima en {ciudad} es {traducir_texto(descripcion, idioma_destino)} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)}°C.'
                    return mensaje_clima
                else:
                    return f'No se encontraron datos para {ciudad}.'
            else:
                return f'No se encontraron datos o no existe {ciudad}'
        else:
            ciudad = obtener_pais_local()
            url = f"{BASE_URL}appid={API_KEY}&q={ciudad}"
            datos_clima = requests.get(url).json()

            if 'main' in datos_clima and 'weather' in datos_clima:
                temp_kelvin = datos_clima['main']['temp']
                temp_celsius = kelvin_a_celsius(temp_kelvin)
                humedad = datos_clima['main']['humidity']
                descripcion = datos_clima['weather'][0]['description']

                idioma_destino = "es"
                mensaje_clima = f'El clima en {ciudad} es {traducir_texto(descripcion, idioma_destino)} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)}°C.'
                return mensaje_clima
            else:
                return f'No se encontraron datos para la {ciudad}.'
    else:
        return False

def obtener_fecha(frase):
    # Verificar si la frase contiene palabras clave
    if "fecha" in frase.lower() or "dia es hoy" in frase.lower():
        fecha_actual = datetime.now()
        # Obtener el nombre del mes y el día
        nombre_mes = fecha_actual.strftime("%B")
        dia = fecha_actual.strftime("%d")
        # Obtener el año
        ano = fecha_actual.strftime("%Y")
        idioma_destino = "es"
        return f"{dia} de {traducir_texto(nombre_mes, idioma_destino)} de {ano}"
    else:
        return False


frase = input("Introduce una frase: ")
if "fecha" in frase.lower() or "dia es hoy" in frase.lower():
    resultado = obtener_fecha(frase)
    print(resultado)
elif "tiempo" in frase.lower() or "clima" in frase.lower():
    resultado = obtener_clima(frase)
    print(resultado)
elif "hora" in frase.lower():
    resultado = obtener_hora(frase)
    print(resultado)

#Usos por partes
"""frase_fecha = input("Introduce una frase: ")
resultado_fecha = obtener_fecha(frase_fecha)
print(resultado_fecha)

frase_clima = input("Ingrese una frase: ")
resultado_clima = obtener_clima(frase_clima)
print(resultado_clima)

frase_hora = input("Ingrese una frase: ")
resultado_hora = obtener_hora(frase_hora)
print(resultado_hora)"""

