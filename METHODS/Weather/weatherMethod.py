# Importar librerias
import json
import requests
# pip install googletrans
from googletrans import Translator
# pip install geopy
from geopy.geocoders import Nominatim

def traducir_texto(texto, destino='en'):
    translator = Translator()
    # Traducimos el texto al idioma destino
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text 

def kelvin_a_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def obtener_pais_local():
    try:
        # Obtenemos la dirección IP del usuario
        ip_info = requests.get('https://ipinfo.io/json')
        ip_data = ip_info.json()

        # Obtenemos las siglas del país desde la información de la IP
        codigo_pais = ip_data.get('country', 'Desconocido')

        # Obtenenemos el nombre completo del país utilizando geolocalización inversa, utilizando las coordenadas anteriores
        url_geolocalizacion = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={ip_data["loc"].split(",")[0]}&lon={ip_data["loc"].split(",")[1]}'
        # Convertimos la respuesta en un dicionario
        respuesta_geolocalizacion = requests.get(url_geolocalizacion)
        datos_geolocalizacion = respuesta_geolocalizacion.json()
        # Extraemos el nombre completo del país
        nombre_pais = datos_geolocalizacion.get('address', {}).get('country', 'Desconocido')

        return nombre_pais
    except Exception as e:
        print(f"Error al obtener la información de la IP: {e}")
        return 'Desconocido'

def obtener_capital(pais):
    # Abrimos el archivo json con la información de países y capitales
    with open(r"paises_capitales.json", "r", encoding="utf-8") as archivo_json:
        # Leemos el contenido y lo cargamos en un diccionario
        data = json.load(archivo_json)
        # Accedemos a la lista de países
        paises = data["paises"] 
        # Traducimos el nombre del pais a Inglés, para que se encuentre en el mismo idioma que en el json
        pais_contexto = "Traduce la siguiente ubicacion: " + pais
        pais_contexto = traducir_texto(pais_contexto, "en")
        pais_name = pais_contexto.split(":", 1)[1].strip()
        # Obtenemos la primera letra del nombre del país y la conviertmos a mayúsculas.
        letra_inicial = pais_name[0].upper()
        # Filtramos la lista de países para obtener solo los que comienzan con la misma letra
        paises_filtrados = [item for item in paises if item["countryName"].startswith(letra_inicial)]
        # Iteramos sobre los países filtrados
        for item in paises_filtrados: 
            # Obtenemos el nombre del país
            country_name = item["countryName"]
            # Vemos si coincide el nombre del país con los del archivo
            if country_name == pais_name:
                # Si es asi, obtenemos el nombre de la capital del país
                capital = item["capital"]
                # Y se traduce al español
                capital_contexto = "Translate this location: " + capital
                capital_contexto = traducir_texto(capital_contexto, "es")
                capital_name = capital_contexto.split(":", 1)[1].strip()
                
                return capital_name
    return False

# Función para obtener los datos del clima a partir de una URL y procesarlos.
def obtener_datos_clima(url):
    # Realizamos una solicitud GET a la URL de la API del clima y convertimos la respuesta a formato JSON
    datos_clima = requests.get(url).json()
    # Verificamos si los datos de la respuesta contienen las claves 'main' y 'weather'
    if 'main' in datos_clima and 'weather' in datos_clima:
        # Extraemos la temperatura en Kelvin de la sección 'main' de los datos del clima
        temp_kelvin = datos_clima['main']['temp']
        # Convertimos la temperatura de Kelvin a Celsius
        temp_celsius = kelvin_a_celsius(temp_kelvin)
        # Extraemos la humedad
        humedad = datos_clima['main']['humidity']
        # Extraemos la descripción del clima de la primera entrada en la lista 'weather'
        descripcion = datos_clima['weather'][0]['description']
        # Corrección de traducción si la descripción es "overcast clouds"
        if descripcion == "overcast clouds":
            descripcion = "nublado"
        # Retornamos los datos del clima en una tupla (temp_celsius, humedad, descripcion)
        return temp_celsius, humedad, descripcion
    else:
        # Si faltan datos en la respuesta de la API, retornamos una tupla de valores nulos
        return None, None, None

def obtener_clima(frase):
    if "tiempo" in frase.lower() or "clima" in frase.lower():
        # Usamos esto para saber si es un país o ciudad real
        geolocator = Nominatim(user_agent="obtener_clima_app")
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "ee8c71bbe4bdc1dfea0d3611a656c853"
        # Verificamos si la frase contiene la palabra "en"
        if "en" in frase.lower():
            # Extraemos la ciudad después de la palabra "en"
            ciudad = frase.split("en", 1)[1].strip()
            # Aquí comprobamos si existe el lugar
            location = geolocator.geocode(ciudad)
            # Comprobamos si es una localización válida
            if location:
                # Traducimos el nombre de la localización a inglés, que es el idioma de la API
                ciudad_contexto = "Traduce la siguiente ubicacion: " + ciudad
                ciudad_contexto_en = traducir_texto(ciudad_contexto, "en")
                ciudad_Ingles = ciudad_contexto_en.split(":", 1)[1].strip()
                # Comprobamos si la localización tiene una capital, por si se introduce una capital
                comprobacion_capital = obtener_capital(ciudad_Ingles)
                # Si no tiene una capital, se busca esa localización
                if comprobacion_capital == False:
                    # Construimos la URL para obtener los datos del clima
                    url = f"{BASE_URL}appid={API_KEY}&q={ciudad_Ingles}"
                    # Obtenemos los datos del clima utilizando la función obtener_datos_clima
                    temp_celsius, humedad, descripcion = obtener_datos_clima(url)
                    # Verificamos si se obtuvieron los datos del clima correctamente
                    if temp_celsius is not None:
                        mensaje_clima = f'El clima en {ciudad.capitalize()} es {traducir_texto(descripcion, "es")} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)} grados Celsius.'
                        return mensaje_clima
                    else:
                        mensaje_error = f'No se encontraron datos para {ciudad}.'
                        return mensaje_error
                else:
                    # Traducimos el nombre de la localización a inglés, que es el idioma de la API
                    capital_contexto = "Traduce la siguiente ubicacion: " + comprobacion_capital
                    capital_contexto = traducir_texto(capital_contexto, "en")
                    capital_contexto = capital_contexto.split(":", 1)[1].strip()
                    # Construimos la URL para obtener los datos del clima, pero en este caso con la capital
                    url = f"{BASE_URL}appid={API_KEY}&q={capital_contexto}"
                    # Obtenemos los datos del clima utilizando la función obtener_datos_clima
                    temp_celsius, humedad, descripcion = obtener_datos_clima(url)
                    # Verificamos si se obtuvieron los datos del clima correctamente
                    if temp_celsius is not None:
                        mensaje_clima = f'El clima en {ciudad.capitalize()}, {comprobacion_capital} es {traducir_texto(descripcion, "es")} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)} grados Celsius.'
                        return mensaje_clima
                    else:
                        mensaje_error = f'No se encontraron datos para {ciudad}.'
                        return mensaje_error
            else:
                mensaje_error = f'No se encontraron datos o no existe {ciudad}'
                return mensaje_error
        else:
            # Si no se ha espedificado ningún lugar concreto se cogera el país local
            ciudad = obtener_pais_local()
            # Obtenemos la capital del país local
            ciudad_local = obtener_capital(ciudad)
            # Construimos la URL para obtener los datos del clima con esa localización
            url = f"{BASE_URL}appid={API_KEY}&q={ciudad_local}"
            # Obtenemos los datos del clima utilizando la función obtener_datos_clima
            temp_celsius, humedad, descripcion = obtener_datos_clima(url)
            # Verificamos si se obtuvieron los datos del clima correctamente
            if temp_celsius is not None:
                mensaje_clima = f'El clima en {ciudad.capitalize()}, {ciudad_local} es {traducir_texto(descripcion, "es")} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)} grados Celsius.'
                return mensaje_clima
            else:
                mensaje_error = f'No se encontraron datos para {ciudad}.'
                return mensaje_error
    else:
        return False


frase = input("Ingrese una frase: ")
resultado = obtener_clima(frase)
print(resultado)

# if __name__ == '__main__':