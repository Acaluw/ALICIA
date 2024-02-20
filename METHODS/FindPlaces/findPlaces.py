import requests
import geocoder


def buscar_restaurantes_cercanos(latitud, longitud, tipo="bar", radio = 10000, limite=10):
    api_key = "AIzaSyCpJ8LYkRE8KYw6GKJ1p4Q_CZH0Ct95iHA"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitud},{longitud}&rankby=distance&type={tipo}&key={api_key}"
    # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitud},{longitud}&rankby=distance&radius={radio}&type={tipo}&key={api_key}"
    response = requests.get(url)
    datos = response.json()
    
    if 'results' in datos:
        restaurantes = datos['results']
        for i, restaurante in enumerate(restaurantes[:limite]):
            nombre = restaurante['name']
            direccion = restaurante['vicinity']
            print(f"{i+1}. Nombre: {nombre}, Dirección: {direccion}")
    else:
        print("No se encontraron restaurantes cercanos.")

from geopy.geocoders import Nominatim

def obtener_latitud_longitud():
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode("Granada")
        
        if location:
            latitud = location.latitude
            longitud = location.longitude
            return latitud, longitud
        else:
            print("No se pudo obtener la ubicación.")
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# latitud = 40.3008
# longitud = -3.4372
# latitud = 37.161377369627836
# longitud = -3.5911357617974686
latitud = 37.19091096796008
longitud = -3.6300729939327936
# latitud = 37.16062868658626
# longitud = -3.5965281246050145
buscar_restaurantes_cercanos(latitud, longitud)
