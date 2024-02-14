# Importar librerias
import json
from googletrans import Translator

def traducir_texto(texto, destino='en'):
    translator = Translator()
    # Traducimos el texto al idioma destino
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text 

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
    return "País no encontrado"

nombre_pais = input("Ingrese el nombre de un país: ")
capital = obtener_capital(nombre_pais)
print(f"La capital de {nombre_pais} es: {capital}")
