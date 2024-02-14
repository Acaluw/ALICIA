# Importar librerias
#https://www.youtube.com/watch?v=TddYMNVV14g&t=886s
import requests
import webbrowser
# Api de google, se tendrán que poner en un archivo aparte
API_key = "AIzaSyCJduRdM7spHTEtxo2lb4CdvrbsClpZkls"
motor_busqueda_key = "b78f092cc4ad449f4"

peticion_busqueda = input("Introduce lo que quieres buscar: ")
# URL base de la API de Google Custom Search
url = "https://www.googleapis.com/customsearch/v1"
# Creamos un diccionario "parametros", que contiene los parámetros de la solicitud HTTP
parametros = {
    # Consulta de búsqueda
    'q' : peticion_busqueda,
    # Clave API
    'key' : API_key,
    # Clave del motor de búsqueda
    'cx' : motor_busqueda_key
}
# Realizamos una solicitud HTTP GET a la URL de la API de Google Custom Search con los parámetros especificados
response = requests.get(url, params = parametros)
# Convertimos la respuesta JSON de la API en un diccionario
resultados = response.json()

if 'items' in resultados:
    # Tomamos los tres primeros resultados
    top_resultados = resultados['items'][:3]  
    for i, result in enumerate(top_resultados, start=1):
        print(f"{i}. {result['link']}")
    # Solicitamos que se elija algún enlace
    seleccion = int(input("Elige el número del enlace que quieres abrir (1-3): "))

    if 1 <= seleccion <= 3:
        enlace_elegido = top_resultados[seleccion - 1]['link']
        print(f"Abriendo: {enlace_elegido}")
        # Abrimos el enlace seleccionado en el navegador web
        webbrowser.open(enlace_elegido)
    else:
        print("Selección no válida. Debes elegir un número del 1 al 3.")
else:
    print("No se encontraron resultados.")
