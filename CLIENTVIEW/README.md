
# ALICIA / @GUI

### Librerías necesarias
```bash
pip install opencv-python-headless Pillow
```

A la hora de elegir el proceso de implementación de una interfaz gráfica, podemos abarcar diversas opciones, pero en este caso se ha optado por lo básico: una interfaz de Tkinter, la cuál viene instalada por defecto en python.

Sin embargo, y siendo la primera versión del proyecto, no se vió oportuno dedicar mucho tiempo aprendiendo y desarrollando la interfaz.

Es aquí donde entra [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer), una herramienta gratuita que permite elegir un diseño elaborado en [Figma](https://www.figma.com) y autogenerar el código correspondiente para Tkinter.

El otro punto a tratar de la interfaz es hablar sobre cómo se gestiona desde esta el funcionamiento del proyecto. Para ello, hacemos uso de Threads.

El proyecto hace uso de un total de 3 Threads + GUI para funcionar:

- Thread para activar/controlar el modelo SpeechToText (métodos) (desde la GUI)
- Thread para controlar el estado del modelo SpeechToText (esperando activación, escuchando petición o solicitud para hacer una captura de webcam) (desde la GUI)
- Thread para inciar el reproductor de música (desde el método [SoundMusic.py](https://github.com/Acaluw/ALICIA/blob/main/METHODS/SoundMusic/soundmusic.py))


Por último, y tal y como se ha mencionado en el segundo Thread, la GUI incorpora una zona de webcam (controlada por OpenCV) que nos permitirá, entre otras cosas, analizar códigos QR al instante o analizar productos (en desarrollo).
