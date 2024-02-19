# Importar librerias
import json
import requests
# pip install googletrans
from googletrans import Translator
# pip install geopy
from geopy.geocoders import Nominatim
# Import credentials file
import cred_weather as cred

def traducir_texto(texto, destino='en'):
    translator = Translator()
    # Translate the text to the language we want
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text 

def kelvin_a_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def obtener_pais_local():
    try:
        # Get the user's IP address
        ip_info = requests.get('https://ipinfo.io/json')
        ip_data = ip_info.json()

        # Obtenemos las siglas del país desde la información de la IP
        codigo_pais = ip_data.get('country', 'Desconocido')

        # Get the full name of the country using reverse geolocation, using the previous coordinates
        url_geolocalizacion = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={ip_data["loc"].split(",")[0]}&lon={ip_data["loc"].split(",")[1]}'
        # Convert the response into a dictionary
        respuesta_geolocalizacion = requests.get(url_geolocalizacion)
        datos_geolocalizacion = respuesta_geolocalizacion.json()
        # Extract the full name of the country
        nombre_pais = datos_geolocalizacion.get('address', {}).get('country', 'Desconocido')

        return nombre_pais
    except Exception as e:
        print(f"Error al obtener la información de la IP: {e}")
        return 'Desconocido'

def obtener_capital(pais):
    # Open the json file with countries and capitals information
    with open(r"paises_capitales.json", "r", encoding="utf-8") as archivo_json:
        # Read the content and load it into a dictionary
        data = json.load(archivo_json)
        # Access the list of countries
        paises = data["paises"] 
        # Translate the country name to English, so it is in the same language as in the json
        pais_contexto = "Traduce la siguiente ubicacion: " + pais
        pais_contexto = traducir_texto(pais_contexto, "en")
        pais_name = pais_contexto.split(":", 1)[1].strip()
        # Get the first letter of the country name and convert it to uppercase.
        letra_inicial = pais_name[0].upper()
        # Filter the list of countries to get only those starting with the same letter
        paises_filtrados = [item for item in paises if item["countryName"].startswith(letra_inicial)]
        # Iterate over the filtered countries
        for item in paises_filtrados: 
            # Get the country name
            country_name = item["countryName"]
            # Check if the country name matches with the name in the file
            if country_name == pais_name:
                # If so, get the name of the country's capital
                capital = item["capital"]
                # And translate it to Spanish
                capital_contexto = "Translate this location: " + capital
                capital_contexto = traducir_texto(capital_contexto, "es")
                capital_name = capital_contexto.split(":", 1)[1].strip()
                
                return capital_name
    return False

# Function to get weather data from a URL and process it
def obtener_datos_clima(url):
    # Make a GET request to the weather API URL and convert the response to JSON format
    datos_clima = requests.get(url).json()
    # Check if the response data contains the keys 'main' and 'weather'
    if 'main' in datos_clima and 'weather' in datos_clima:
        # Extract the temperature in Kelvin from the 'main' section of the weather data
        temp_kelvin = datos_clima['main']['temp']
        # Convert temperature from Kelvin to Celsius
        temp_celsius = kelvin_a_celsius(temp_kelvin)
        # Extract humidity
        humedad = datos_clima['main']['humidity']
        # Extract weather description from the first entry in the 'weather' list
        descripcion = datos_clima['weather'][0]['description']
        # Translation correction if the description is "overcast clouds"
        if descripcion == "overcast clouds":
            descripcion = "nublado"
        # Return weather data in a tuple (temp_celsius, humidity, description)
        return temp_celsius, humedad, descripcion
    else:
        # If data is missing in the API response, return a tuple of null values
        return None, None, None

def obtener_clima(frase):
    # Check if the words "tiempo" or "clima" are in the sentence
    if "tiempo" in frase.lower() or "clima" in frase.lower():
        # Use this to know if it's a real country or city
        geolocator = Nominatim(user_agent="obtener_clima_app")
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = cred.api_key
        # Check if the sentence contains the word "en"
        if "en" in frase.lower():
            # Extract the city after the word "in"
            ciudad = frase.split("en", 1)[1].strip()
            # Check if it's a valid location, if the place exists
            location = geolocator.geocode(ciudad)
            if location:
                # Translate the location name to English, which is the language of the API
                ciudad_contexto = "Traduce la siguiente ubicacion: " + ciudad
                ciudad_contexto_en = traducir_texto(ciudad_contexto, "en")
                ciudad_Ingles = ciudad_contexto_en.split(":", 1)[1].strip()
                # Check if the location has a capital, in case a capital or other place is entered
                comprobacion_capital = obtener_capital(ciudad_Ingles)
                # If it doesn't have a capital, we will look for that location
                if comprobacion_capital == False:
                    # Build the URL to get weather data
                    url = f"{BASE_URL}appid={API_KEY}&q={ciudad_Ingles}"
                    # Get weather data using the obtener_datos_clima function
                    temp_celsius, humedad, descripcion = obtener_datos_clima(url)
                    # Check if weather data was obtained successfully
                    if temp_celsius is not None:
                        mensaje_clima = f'El clima en {ciudad.capitalize()} es {traducir_texto(descripcion, "es")} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)} grados Celsius.'
                        return mensaje_clima
                    else:
                        mensaje_error = f'No se encontraron datos para {ciudad}.'
                        return mensaje_error
                else:
                    # Translate the location name to English, which is the language of the API
                    capital_contexto = "Traduce la siguiente ubicacion: " + comprobacion_capital
                    capital_contexto = traducir_texto(capital_contexto, "en")
                    capital_contexto = capital_contexto.split(":", 1)[1].strip()
                    # Build the URL to get weather data, but in this case with th capital 
                    url = f"{BASE_URL}appid={API_KEY}&q={capital_contexto}"
                    # Get weather data using the obtener_datos_clima function
                    temp_celsius, humedad, descripcion = obtener_datos_clima(url)
                    # Check if weather data was obtained successfully
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
            # If no specific location is provided, the local country will be taken
            ciudad = obtener_pais_local()
            # Get the capital of the local country
            ciudad_local = obtener_capital(ciudad)
            # Build the URL to get weather data, but in this case with th capital 
            url = f"{BASE_URL}appid={API_KEY}&q={ciudad_local}"
            # Get weather data using the obtener_datos_clima function
            temp_celsius, humedad, descripcion = obtener_datos_clima(url)
            # Check if weather data was obtained successfully
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

"""if __name__ == '__main__':
    peticion_busqueda = input("De que país quieres saber la capital: ")
    obtener_clima(peticion_busqueda)"""