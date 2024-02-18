# Importar librerias
#https://www.youtube.com/watch?v=TddYMNVV14g&t=886s
import requests
import webbrowser
# Api de google, se tendrán que poner en un archivo aparte
API_key = "AIzaSyCJduRdM7spHTEtxo2lb4CdvrbsClpZkls"
motor_busqueda_key = "b78f092cc4ad449f4"

def googleSearch(keyword):
    # URL base de la API de Google Custom Search
    url = "https://www.googleapis.com/customsearch/v1"
    # Creamos un diccionario "parametros", que contiene los parámetros de la solicitud HTTP
    parametros = {
        # Consulta de búsqueda
        'q' : keyword,
        # Clave API
        'key' : API_key,
        # Clave del motor de búsqueda
        'cx' : motor_busqueda_key
    }
    # Realizamos una solicitud HTTP GET a la URL de la API de Google Custom Search con los parámetros especificados
    response = requests.get(url, params = parametros)
    # Convertimos la respuesta JSON de la API en un diccionario
    resultados = response.json()
    # Comprobamos si hay elementos de búsqueda en los resultados
    if 'items' in resultados:
        # Extraemos le primer enlace
        enlace = resultados['items'][0]['link']
        print(resultados['items'][0]['link'])
        # Abrimos el enlace en el navegador web
        webbrowser.open(enlace)

if __name__ == '__main__':
    peticion_busqueda = input("Introduce lo que quieres buscar: ")
    googleSearch(peticion_busqueda)