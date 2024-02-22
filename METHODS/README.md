
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

En este repositorio se presenta una colección de métodos desarrollados para una variedad de tareas concretas que realizará nuestro asistente virtual. Cada método se centra en una funcionalidad específica, desde la búsqueda de información hasta el control de dispositivos. A continuación, se detallan los métodos disponibles junto con una breve descripción de su funcionalidad.

### CapitalCountry

En este método, utilizamos la bibioteca de "googletrans" para traducir textos y la librería "json" para poder abrir el archivo JSON, llamado "paises_capitales.json" que contiene todos los paises y sus capitales correspondientes. 
El usuario proporciona el nombre de algún país el cuál quiera saber su capital y el método devuleve la capital correspondiente, utilizando la traducción para que el país se encuentre en el mismo idioma que en el JSON (ubicado en TEMPFILES).

### FindPlaces

Este método permite buscar tanto restaurantes, bares, hospitales, etc... cercanos a una ubicación específica utilizando la API de Google Places. Se importan las bibliotecas necesarias, como "requests" y "geopy".
Se solicita al usuario una ubicación y un tipo de lugar y se busca y muestra los restaurantes cercanos a esa ubicación que coincidan con el tipo especificado.

### GoogleSearch

En este método, utilizamos la API de Google Custom Search para realizar búsquedas en la web. Se importan las bibliotecas necesarias, como "requests" y "webbrowser". Este método toma una palabra clave y construye un solicitud http con los párametros específicos, después se recuperan los resultados en formato JSON, extraemos y abrimos el primer enlace.

### QRCode

Este método se encarga de detectar y decodificar posibles códigos QR en una imagen. Se importan las bibliotecas necesarias, como "cv2" para procesamiento de imágenes y "webbrowser" para abrir enlaces web. 
Básicamente, si se encuentra un código QR válido, se imprime el dato decodificado y se abre la URL correspondiente en el navegador web.

### SoundMusic

El fichero SoundMusic recopila toda la lógica referente a reproducir sonidos desde el asistente. Este recibe un input a buscar (se le asigna letra/lyrics para un audio más legible), lo descarga en la carpeta TEMPFILES (no se le da un formato para evitar fichero corrupto) y, por último, utilizamos la biblioteca vlc para reproducir dicho audio. Esta biblioteca inicia un hilo independiente del programa principal para evitar que la interfaz o el modelo speech se quede bloqueado. Por último, cabe destacar que tenemos las opciones de poder pausar, reanudar y parar el audio en todo momento.

### Time

Este método proporciona funcionalidades relacionadas con la fecha y la hora. Se utilizan varias bibliotecas, como "datetime", "pytz", "pycountry" y "googletrans", para realizar tareas específicas.
Lo que permite al usuario este método es obtener información sobre la fecha y la hora actual de una ubicación específica.

### VolumeControl

El método VolumeControl permite al asistente modificar el volumen del sistema dependiendo de la solicitud recibida. Para ello, detecta el sistema que está usando y, dependiendo de este, ajusta el volumen de una manera u otra (en windows mediante una escala de -65.25db a 0db y el uso de la librería 'pycaw', y en linux directamente mediante el comando 'amixer').

### Weather

Este método proporciona funcionalidades relacionadas con la obtención de datos meteorológicos. Se utilizan varias bibliotecas, como "requests", "googletrans", "pytz", "geopy" y "json", para realizar diferentes tareas.
Permite al usuario preguntar por algún país o ciudad, para saber la información meteorológica actual para esa ubicación, incluyendo la temperatura, la humedad y la descripción del clima. Si se introduce un país el método calculara su capital automáticamente y dirá la información meteorológica de este.

### (No usada) TimeDate 

Este método proporciona funcionalidades relacionadas con la obtención de la hora y la fecha actual en diferentes ubicaciones. Se utilizan varias bibliotecas, como geopy, datetime, timezonefinder, pytz, y googletrans, para realizar estas tareas.
Este utiliza la geolocalización inversa para determinar las coordenadas geográficas de la ubicación proporcionada y luego utiliza timezonefinder para obtener la zona horaria asociada a esas coordenadas, es decir, le puedes preguntar sobre la hora en cualquier parte del mundo, país o ciudad, pero timezonefinder actualmente no es compatible con python 3.12.

