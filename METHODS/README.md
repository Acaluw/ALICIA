
# ALICIA / @METHODS

### Librerías necesarias
```bash
pip install pytube
pip install python-vlc
pip install pycaw
pip install requests
pip install googletrans
pip install geopy
pip install geocoder
pip install pycountry
pip install pytz
pip install webbrowser
```

### (Aqui va una introducción)En este repositorio, llamado METHODS, se presenta una colección de métodos desarrollados para una variedad de tareas para nuestro asistente virtual. Cada método se centra en una funcionalidad específica, desde la búsqueda de información hasta el control de dispositivos. A continuación, se detallan los métodos disponibles junto con una breve descripción de su funcionalidad.

### CapitalCountry

En este método, utilizamos la bibioteca de "googletrans" para traducir textos y la libreria "json" para poder abrir el archivo JSON, llamado "paises_capitales.json" que contiene todos los paises y sus capitales correspondientes. 
El usuario proporciona el nombre de algún país el cuál quiera saber su capital y el método devuleve la capital correspondiente, utilizando la traducción para que el país se encuentre en el mismo idioma que en el JSON.

### FindPlaces

Este método permite buscar tanto restaurantes, bares, hospitales, etc... cercanos a una ubicación específica utilizando la API de Google Places. Se importan las bibliotecas necesarias, como "requests" y "geopy".
Se solicita al usuario una ubicación y un tipo de lugar y se busca y muestra los restaurantes cercanos a esa ubicación que coincidan con el tipo especificado.

### GoogleSearch

En este método, utilizamos la API de Google Custom Search para realizar búsquedas en la web. Se importan las bibliotecas necesarias, como "requests" y "webbrowser". Este método toma una palabra clave y construye un solicitud http con los párametros específicos, después se recuperamos los resultados en formato JSON y extraemos y abrimos el primer enlace.

### QRCode

Este método se encarga de detectar y decodificar posibles códigos QR en una imagen. Se importan las bibliotecas necesarias, como "cv2" para procesamiento de imágenes y "webbrowser" para abrir enlaces web. 
Básicamente, si se encuentra un código QR válido, se imprime el dato decodificado y se abre la URL correspondiente en el navegador web.

### SoundMusic

Este método proporciona funcionalidades para descargar y reproducir audio desde YouTube. Se importan las bibliotecas necesarias, como pytube para la manipulación de videos de YouTube y python-vlc para la reproducción de audio. 
En resumen, solicita al usuario una consulta de búsqueda de video, descarga el audio del primer resultado relacionado con esa consulta, lo reproduce y ofrece la opción de pausar, reanudar o quitar la reproducción.

### Time

Este método proporciona funcionalidades relacionadas con la fecha y la hora. Se utilizan varias bibliotecas, como "datetime", "pytz", "pycountry" y "googletrans", para realizar tareas específicas.
Lo que permite al usuario este método es obtener información sobre la fecha y la hora actual de una ubicación específica.

### VolumeControl

texto

### Weather

Este método proporciona funcionalidades relacionadas con la obtención de datos meteorológicos. Se utilizan varias bibliotecas, como "requests", "googletrans", "pytz", "geopy" y "json", para realizar diferentes tareas.
Permite al usuario preguntar por algún país o ciudad, para saber la información meteorológica actual para esa ubicación, incluyendo la temperatura, la humedad y la descripción del clima. Si se introduce un país el método calculara su capital automáticamente y dirá la información meteorológica de este.

### (No usada) TimeDate 

Este método proporciona funcionalidades relacionadas con la obtención de la hora y la fecha actual en diferentes ubicaciones. Se utilizan varias bibliotecas, como geopy, datetime, timezonefinder, pytz, y googletrans, para realizar estas tareas.
Este utiliza la geolocalización inversa para determinar las coordenadas geográficas de la ubicación proporcionada y luego utiliza timezonefinder para obtener la zona horaria asociada a esas coordenadas, es decir, le puedes preguntar sobre la hora en cualquier parte del mundo, país o ciudad, pero timezonefinder actualmente no es compatible con python 3.12.

