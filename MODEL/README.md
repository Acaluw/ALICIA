
# ALICIA / @Models

Actualmente, ALICIA cuenta con tres modelos, utilizados para la interacción con el usuario. Estos son:

### Rekognition_V1
#### Librerías necesarias
```bash
pip install boto3
```
Este modelo permite, gracias a una imagen obtenida vía webcam mediante la petición del usuario, analizar dicha imagen en busca de productos que buscar en comercios online.

Este análisis se realiza mediante el plugin Rekognition de AWS, por lo que, para poder hacer uso de dicho modelo, se deberá disponer de una cuenta de AWS y actualizar las variables del fichero 'rekogCreds.py' con las proporcionadas por el laboratorio de su cuenta.

Por defecto, este modelo no viene activado en el resultado final, ya que los resultados obtenidos no se acercan a lo esperado, además del detalle de las credenciales.

### SpeechToText_V1
#### Librerías necesarias
```bash
pip install SpeechRecognition
```
El modelo de SpeechToText_V1 hace uso de la biblioteca SpeechRecognition para poder recibir la petición del usuario.

El funcionamiento es el siguiente:
- Se crea una instancia del micrófono del equipo, que permanecerá activo en todo momento esperando la palabra de activación o la petición.
- Por otro lado, contamos con una variable de reconocimiento que actúa de forma dual, limpiando el audio reconocido, y analizando mediante google (lengua por defecto español) la petición recibida.
- Una vez tenemos la petición en formato texto, se analiza el contenido y se ejecuta la función correspondiente.

Como aportación adicional, este modelo hace uso de eventos, ya que en la interfaz gráfica, este es llamado por un Thread, lo que nos permite controlar diferentes elementos de esta, así como permitir el flujo constante entre GUI y SpeechToText.

### TextToSpeech_V1
#### Librerías necesarias
```bash
pip install pyttsx3
```
El modelo de TextToSpeech_V1 hace uso de la biblioteca pyttsx3 para que la propia máquina lea en voz alta el resultado de las peticiones del usuario.

El funcionamiento es el siguiente:
- Inicializamos el motor de pyttsx3. Este motor contiene ciertas propiedades que pueden ser modificadas a gusto. En este caso, se ha reducido la cantidad de palabras por minuto que se lee, con el fin de obtener un resultado agradable para el usuario.
- El modelo contiene una serie de funciones, las cuales son llamadas por el modelo de SpeechToText_V1, que a su vez, ejecutan las funciones correspondientes, mientras que la máquina lee en voz alta la acción que va a realizar.
