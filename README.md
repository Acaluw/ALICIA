# Asistente por voz ALICIA (WIP)

ALICIA es un proyecto propuesto en clase con el propósito de integrar el uso de inteligencia artifical de bajo nivel.

En el caso de este proyecto, la inteligencia artifical reside en la posibilidad de transcribir, tanto la voz del usuario a texto, como leer el resultado devuelto por la máquina.

Además, también se cuenta con un modelo que analiza un producto mostrado por cámara (AWS), con la intención de buscar a través de una plataforma de comercio. (Este modelo no presenta resultados acertados y son meramente orientativos a lo que se analiza en la imagen)

## Autores

- [@Acaluw (Juan Barrera)](https://github.com/Acaluw)

- [@AndresPinilla1](https://github.com/AndresPinilla1)

## Guía de proyecto

- Modelos (Transcripciones y análisis de productos)

- Métodos generales (control de volumen, reproductor de audio, etc)

- GUI (Uso de Tkinter Designer, threads y webcam)

## Instalación de librerías

Este proyecto ha sido desarrollado bajo [Python 3.12.0.](https://www.python.org/downloads/release/python-3120/) El uso de una versión superior o inferior puede ocasionar errores de compilación.

Para poder hacer uso completo de las funcionalidades del proyecto, se deberán instalar además las siguientes librerías:

### GUI

```bash
pip install opencv-python-headless Pillow
```

### Modelo de transcripción voz -> texto

```bash
pip install SpeechRecognition
```

### Modelo de transcripción texto -> voz

```bash
pip install pyttsx3
```

### Modelo de análisis de productos (AWS)

```bash
pip install boto3
```

### Métodos generales

```bash
pip install pytube
pip install python-vlc
pip install pycaw
pip install requests
pip install googletrans==4.0.0-rc1
pip install geopy
pip install geocoder
pip install pycountry
pip install pytz
pip install webbrowser
```

Como complemento, se deberá instalar vlc en el equipo y tener este visible desde las variables de entorno. Puedes obtener la última versión de VLC en el siguiente [enlace.](https://www.videolan.org/vlc/index.es.html)

# ALICIA / @METHODS

En este repositorio se presenta una colección de métodos desarrollados para una variedad de tareas concretas que realizará nuestro asistente virtual. Cada método se centra en una funcionalidad específica, desde la búsqueda de información hasta el control de dispositivos. A continuación, se detallan los métodos disponibles junto con una breve descripción de su funcionalidad.

### `CapitalCountry`

En este método, utilizamos la bibioteca de "googletrans" para traducir textos y la librería "json" para poder abrir el archivo JSON, llamado "paises_capitales.json" que contiene todos los paises y sus capitales correspondientes.
El usuario proporciona el nombre de algún país el cuál quiera saber su capital y el método devuleve la capital correspondiente, utilizando la traducción para que el país se encuentre en el mismo idioma que en el JSON (ubicado en TEMPFILES).

```bash
palabras clave: 'capital' y 'de' en la petición
```

### `FindPlaces`

Este método permite buscar tanto restaurantes, bares, hospitales, etc... cercanos a una ubicación específica utilizando la API de Google Places. Se importan las bibliotecas necesarias, como "requests" y "geopy".
Se solicita al usuario una ubicación y un tipo de lugar y se busca y muestra los restaurantes cercanos a esa ubicación que coincidan con el tipo especificado.

```bash
palabras clave: 'encuentra' y ('cercanos en' o 'cercanos por') en la petición
```

### `GoogleSearch`

En este método, utilizamos la API de Google Custom Search para realizar búsquedas en la web. Se importan las bibliotecas necesarias, como "requests" y "webbrowser". Este método toma una palabra clave y construye un solicitud http con los párametros específicos, después se recuperan los resultados en formato JSON, extraemos y abrimos el primer enlace.

```bash
palabras clave: 'busca' en la petición
```

### `QRCode`

Este método se encarga de detectar y decodificar posibles códigos QR en una imagen. Se importan las bibliotecas necesarias, como "cv2" para procesamiento de imágenes y "webbrowser" para abrir enlaces web.
Básicamente, si se encuentra un código QR válido, se imprime el dato decodificado y se abre la URL correspondiente en el navegador web.

```bash
palabras clave: ('escanea' o 'busca') y 'código' en la petición
```

### `SoundMusic`

El fichero SoundMusic recopila toda la lógica referente a reproducir sonidos desde el asistente. Este recibe un input a buscar (se le asigna letra/lyrics para un audio más legible), lo descarga en la carpeta TEMPFILES (no se le da un formato para evitar fichero corrupto) y, por último, utilizamos la biblioteca vlc para reproducir dicho audio (se le asigna el tiempo concreto de duración para evitar sonido vacío). Esta biblioteca inicia un hilo independiente del programa principal para evitar que la interfaz o el modelo speech se quede bloqueado. Por último, cabe destacar que tenemos las opciones de poder pausar, reanudar y parar el audio en todo momento.

```bash
palabras clave:
Reproducir -> 'reproduce' o 'pon' en la petición
Pausar -> 'pausa' en la petición
Reanudar -> 'continúa' o 'reanuda' en la petición
Parar -> ('para' o 'quita') y 'canción' en la petición
```

### `Time`

Este método proporciona funcionalidades relacionadas con la fecha y la hora. Se utilizan varias bibliotecas, como "datetime", "pytz", "pycountry" y "googletrans", para realizar tareas específicas.
Lo que permite al usuario este método es obtener información sobre la fecha y la hora actual de una ubicación específica.

```bash
palabras clave:
Hora local -> 'hora es' en la petición
Hora en lugar concreto -> 'hora es' y 'en' en la petición
Día actual -> 'día es hoy' en la petición
```

### `VolumeControl`

El método VolumeControl permite al asistente modificar el volumen del sistema dependiendo de la solicitud recibida. Para ello, detecta el sistema que está usando y, dependiendo de este, ajusta el volumen de una manera u otra (en windows mediante una escala de -65.25db a 0db y el uso de la librería 'pycaw', y en linux directamente mediante el comando 'amixer').

```bash
palabras clave: 'Volumen' y 'al' en la petición
```

### `Weather`

Este método proporciona funcionalidades relacionadas con la obtención de datos meteorológicos. Se utilizan varias bibliotecas, como "requests", "googletrans", "pytz", "geopy" y "json", para realizar diferentes tareas.
Permite al usuario preguntar por algún país o ciudad, para saber la información meteorológica actual para esa ubicación, incluyendo la temperatura, la humedad y la descripción del clima. Si se introduce un país el método calculara su capital automáticamente y dirá la información meteorológica de este.

```bash
palabras clave: ('tiempo' o 'clima') y 'en' en la petición
```

# ALICIA / @Models

Actualmente, ALICIA cuenta con tres modelos, utilizados para la interacción con el usuario. Estos son:

### Rekognition_V1

Este modelo permite, gracias a una imagen obtenida vía webcam mediante la petición del usuario, analizar dicha imagen en busca de productos que buscar en comercios online.

Este análisis se realiza mediante el plugin Rekognition de AWS, por lo que, para poder hacer uso de dicho modelo, se deberá disponer de una cuenta de AWS y actualizar las variables del fichero 'rekogCreds.py' con las proporcionadas por el laboratorio de su cuenta.

Por defecto, este modelo no viene activado en el resultado final, ya que los resultados obtenidos no se acercan a lo esperado, además del detalle de las credenciales.

### SpeechToText_V1

El modelo de SpeechToText_V1 hace uso de la biblioteca SpeechRecognition para poder recibir la petición del usuario.

El funcionamiento es el siguiente:

- Se crea una instancia del micrófono del equipo, que permanecerá activo en todo momento esperando la palabra de activación o la petición.
- Por otro lado, contamos con una variable de reconocimiento que actúa de forma dual, limpiando el audio reconocido, y analizando mediante google (lengua por defecto español) la petición recibida.
- Una vez tenemos la petición en formato texto, se analiza el contenido y se ejecuta la función correspondiente.

Como aportación adicional, este modelo hace uso de eventos, ya que en la interfaz gráfica, este es llamado por un Thread, lo que nos permite controlar diferentes elementos de esta, así como permitir el flujo constante entre GUI y SpeechToText.

### TextToSpeech_V1

El modelo de TextToSpeech_V1 hace uso de la biblioteca pyttsx3 para que la propia máquina lea en voz alta el resultado de las peticiones del usuario.

El funcionamiento es el siguiente:

- Inicializamos el motor de pyttsx3. Este motor contiene ciertas propiedades que pueden ser modificadas a gusto. En este caso, se ha reducido la cantidad de palabras por minuto que se lee, con el fin de obtener un resultado agradable para el usuario.
- El modelo contiene una serie de funciones, las cuales son llamadas por el modelo de SpeechToText_V1, que a su vez, ejecutan las funciones correspondientes, mientras que la máquina lee en voz alta la acción que va a realizar.

# ALICIA / @GUI

A la hora de elegir el proceso de implementación de una interfaz gráfica, podemos abarcar diversas opciones, pero en este caso se ha optado por lo básico: una interfaz de Tkinter, la cuál viene instalada por defecto en python.

Sin embargo, y siendo la primera versión del proyecto, no se vió oportuno dedicar mucho tiempo aprendiendo y desarrollando la interfaz.

Es aquí donde entra [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer), una herramienta gratuita que permite elegir un diseño elaborado en [Figma](https://www.figma.com) y autogenerar el código correspondiente para Tkinter.

El otro punto a tratar de la interfaz es hablar sobre cómo se gestiona desde esta el funcionamiento del proyecto. Para ello, hacemos uso de Threads.

El proyecto hace uso de un total de 3 Threads + GUI para funcionar:

- Thread para activar/controlar el modelo SpeechToText (métodos) (desde la GUI)
- Thread para controlar el estado del modelo SpeechToText (esperando activación, escuchando petición o solicitud para hacer una captura de webcam) (desde la GUI)
- Thread para inciar el reproductor de música (desde el método [SoundMusic.py](https://github.com/Acaluw/ALICIA/blob/main/METHODS/SoundMusic/soundmusic.py))

Por último, y tal y como se ha mencionado en el segundo Thread, la GUI incorpora una zona de webcam (controlada por OpenCV) que nos permitirá, entre otras cosas, analizar códigos QR al instante o analizar productos (en desarrollo).
