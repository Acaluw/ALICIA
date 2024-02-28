# Importar librerias
#https://www.youtube.com/watch?v=TddYMNVV14g&t=886s
import requests
import webbrowser
import os
from dotenv import load_dotenv

load_dotenv()
# Google API
API_key = os.getenv("GOOGLEKEY")
motor_busqueda_key = os.getenv("MOTORKEY")

# googleSearch(keyword: string) -> Performs a google search for the keyword value
def googleSearch(keyword):
    # Basic URL of Google Custom Search API
    url = "https://www.googleapis.com/customsearch/v1"
    # Create a dictionary "parametros", which contains the parameters of the HTTP request
    parametros = {
        # Search query
        'q' : keyword,
        # API Key
        'key' : API_key,
        # Search engine key
        'cx' : motor_busqueda_key
    }
    # Make an HTTP GET request to the Google Custom Search API URL with the specified parameters
    response = requests.get(url, params = parametros)
    # Convert the JSON response from the API into a dictionary
    resultados = response.json()
    # Check if there are search items in the results
    if 'items' in resultados:
        # Extract the first link
        enlace = resultados['items'][0]['link']
        print(resultados['items'][0]['link'])
        # Open the link in the web browser
        webbrowser.open(enlace)

if __name__ == '__main__':
    peticion_busqueda = input("Introduce lo que quieres buscar: ")
    googleSearch(peticion_busqueda)