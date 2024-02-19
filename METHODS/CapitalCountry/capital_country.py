# Importing libraries
import json
from googletrans import Translator

def traducir_texto(texto, destino='en'):
    translator = Translator()
    # Translate the text to the language we want
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text 

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
    return "País no encontrado"
"""
if __name__ == '__main__':
    peticion_busqueda = input("De que país quieres saber la capital: ")
    obtener_capital(peticion_busqueda)"""

nombre_pais = input("Ingrese el nombre de un país: ")
capital = obtener_capital(nombre_pais)
print(f"La capital de {nombre_pais} es: {capital}")
