
# Asistente por voz ALICIA (WIP)

ALICIA es un proyecto propuesto en clase con el propósito de integrar el uso de inteligencia artifical de bajo nivel. 

En el caso de este proyecto, la inteligencia artifical reside en la posibilidad de transcribir, tanto la voz del usuario a texto, como leer el resultado devuelto por la máquina. 

Además, también se cuenta con un modelo que analiza un producto mostrado por cámara (AWS), con la intención de buscar a través de una plataforma de comercio. (Este modelo no presenta resultados acertados y son meramente orientativos a lo que se analiza en la imagen)

## Autores

- [@Acaluw (Juan Barrera)](https://github.com/Acaluw)

- [@AndresPinilla1](https://github.com/AndresPinilla1)
## Guía de proyecto

- [Modelos (Transcripciones y análisis de productos)](https://github.com/Acaluw/ALICIA/tree/main/MODEL)

- [Métodos generales (control de volumen, reproductor de audio, etc)](https://github.com/Acaluw/ALICIA/tree/main/METHODS)

- [GUI (Uso de Tkinter Designer, threads y webcam)](https://github.com/Acaluw/ALICIA/tree/main/CLIENTVIEW)
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
pip install googletrans
pip install geopy
pip install geocoder
```

Como complemento, se deberá instalar vlc en el equipo y tener este visible desde las variables de entorno. Puedes obtener la última versión de VLC en el siguiente [enlace.](https://www.videolan.org/vlc/index.es.html)
