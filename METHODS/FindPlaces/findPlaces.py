# pip install requests
# pip install geopy
# pip install geocoder

import requests
import geocoder
from geopy.geocoders import Nominatim

def buscar_place_cercanos(latitud, longitud, tipo = "", radio = 10000, limite=10):
    tipo = busqueda_tipo(tipo)
    api_key = "AIzaSyCpJ8LYkRE8KYw6GKJ1p4Q_CZH0Ct95iHA"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitud},{longitud}&rankby=distance&type={tipo}&key={api_key}"
    response = requests.get(url)
    datos = response.json()
    
    if 'results' in datos:
        places = datos['results']
        for i, place in enumerate(places[:limite]):
            nombre = place['name']
            direccion = place['vicinity']
            print(f"{i+1}. Nombre: {nombre}, Dirección: {direccion}")
    else:
        print(f"Methods || FindPlaces: No se encontraron {tipo} cercanos.")

def busqueda_tipo(frase):
    tipos_disponibles = {
        "restaurante": "restaurant",
        "cafe": "cafe",
        "bar": "bar",
        "panaderia": "bakery",
        "supermercado": "grocery_or_supermarket",
        "hospital": "hospital",
        "farmacia": "pharmacy",
        "banco": "bank",
        "cajero": "atm",
        "parque": "park",
        "gimnasio": "gym",
        "cine": "movie_theater",
        "teatro": "movie_theater",
        "centro comercial": "shopping_mall",
        "centros comerciales": "shopping_mall",
        "libreria": "book_store",
        "gasolinera": "gas_station",
        "estacion de tren": "train_station",
        "estaciones de trenes": "train_station",
        "aeropuerto": "airport",
        "estacion de autobus": "bus_station",
        "estaciones de autobuses": "bus_station",
        "parada de autobus": "bus_station",
        "paradas de autobus": "bus_station",
        "parada de taxi": "taxi_stand",
        "paradas de taxi": "taxi_stand",
        "alojamiento": "lodging",
        "hotel": "lodging"
    }
    
    for palabra, tipo in tipos_disponibles.items():
        if palabra in frase.lower():
            return tipo
    
    return None

def obtener_latitud_longitud(input):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(input)
        
        if location:
            latitud = location.latitude
            longitud = location.longitude
            return latitud, longitud
        else:
            print("Methods || FindPlaces: No se pudo obtener la ubicación.")
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

if __name__ == "__main__":
    zona = input("Introduce la zona: ")
    tipo = input("Introduce tipo: ")
    latitud, longitud = obtener_latitud_longitud(zona)
    buscar_place_cercanos(latitud, longitud, tipo=tipo)
