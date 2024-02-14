# Importar librerias
import json
import requests
from googletrans import Translator
from geopy.geocoders import Nominatim

def traducir_texto(texto, destino='en'):
    translator = Translator()
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text

def kelvin_a_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

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

def obtener_capital(pais):
    with open(r"C:\Users\Andre\Desktop\Python_VSC\Alice-AI\paises_capitales.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        paises = data["paises"]  # Acceder a la lista de países
        
        pais_contexto = "Traduce la siguiente ubicacion: " + pais
        pais_contexto = traducir_texto(pais_contexto, "en")
        pais_name = pais_contexto.split(":", 1)[1].strip()
        
        letra_inicial = pais_name[0].upper()  # Obtener la letra inicial del país
        # Filtrar la lista de países para obtener solo los que comienzan con la misma letra
        paises_filtrados = [item for item in paises if item["countryName"].startswith(letra_inicial)]

        for item in paises_filtrados:  # Iterar sobre los países filtrados
            country_name = item["countryName"]
            if country_name == pais_name:
                capital = item["capital"]
                capital_contexto = "Translate this location: " + capital
                capital_contexto = traducir_texto(capital_contexto, "es")
                capital_name = capital_contexto.split(":", 1)[1].strip()
                
                return capital_name
    return False

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
                ciudad_contexto = "Traduce la siguiente ubicacion: " + ciudad
                ciudad_contexto_en = traducir_texto(ciudad_contexto, "en")
                ciudad_Ingles = ciudad_contexto_en.split(":", 1)[1].strip()
                comprobacion_capital = obtener_capital(ciudad_Ingles)
                
                if comprobacion_capital == False:
                    url = f"{BASE_URL}appid={API_KEY}&q={ciudad_Ingles}"
                    datos_clima = requests.get(url).json()
                    
                    if 'main' in datos_clima and 'weather' in datos_clima:
                        temp_kelvin = datos_clima['main']['temp']
                        temp_celsius = kelvin_a_celsius(temp_kelvin)
                        humedad = datos_clima['main']['humidity']
                        descripcion = datos_clima['weather'][0]['description']
                        #Correccion de traducción 
                        if descripcion == "overcast clouds":
                            descripcion = "nublado"

                        idioma_destino = "es"
                        mensaje_clima = f'El clima en {ciudad.capitalize()} es {traducir_texto(descripcion, idioma_destino)} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)}°C.'
                        return mensaje_clima
                    else:
                        return f'No se encontraron datos para {ciudad}.'
                    
                else:
                    capital_contexto = "Traduce la siguiente ubicacion: " + comprobacion_capital
                    capital_contexto = traducir_texto(capital_contexto, "en")
                    capital_contexto = capital_contexto.split(":", 1)[1].strip()
                    
                    url = f"{BASE_URL}appid={API_KEY}&q={capital_contexto}"
                    datos_clima = requests.get(url).json()
                    
                    if 'main' in datos_clima and 'weather' in datos_clima:
                        temp_kelvin = datos_clima['main']['temp']
                        temp_celsius = kelvin_a_celsius(temp_kelvin)
                        humedad = datos_clima['main']['humidity']
                        descripcion = datos_clima['weather'][0]['description']
                        #Correccion de traducción 
                        if descripcion == "overcast clouds":
                            descripcion = "nublado"

                        idioma_destino = "es"
                        mensaje_clima = f'El clima en {ciudad.capitalize()}, {comprobacion_capital} es {traducir_texto(descripcion, idioma_destino)} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)}°C.'
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
                mensaje_clima = f'El clima en {ciudad.capitalize()} es {traducir_texto(descripcion, idioma_destino)} con una humedad de {humedad}% y una temperatura de {round(temp_celsius, 2)}°C.'
                return mensaje_clima
            else:
                return f'No se encontraron datos para la {ciudad}.'
    else:
        return False

frase = input("Ingrese una frase: ")
resultado = obtener_clima(frase)
print(resultado)
