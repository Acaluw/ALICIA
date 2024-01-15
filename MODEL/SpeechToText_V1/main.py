# Libs import
import sys
from pathlib import Path
import speech_recognition as sr
import threading

# Making TextToSpeech/main.py visible for this file
root_path = Path(__file__).resolve().parents[1]
sys.path.append(str(root_path))
from TextToSpeech_V1 import main as tts

# Main Variables
voiceRecog = sr.Recognizer()
activeBool = False
activeModel = threading.Event()

# Method that listen for a keyword to activate listen() method
def listenKeyWord():
    with sr.Microphone() as source:
        print("...")
        voiceRecog.adjust_for_ambient_noise(source, duration=1)
        audio = voiceRecog.listen(source)

    try:
        texto = voiceRecog.recognize_google(audio, language='es')
        print(texto)
        if 'Alicia' in texto:
            return True
    except sr.UnknownValueError:
        return False

# Method that listen for a current command
def listen():
    with sr.Microphone() as source:
        print("Command section...")
        voiceRecog.adjust_for_ambient_noise(source, duration=1)
        audio = voiceRecog.listen(source)

    try:
        texto = voiceRecog.recognize_google(audio,language='es')
        print("Command detected...")
        return texto.lower()
    except sr.UnknownValueError:
        return ""
    
# Active loop that keep listening for the keyword
def runSpeechModel():
    global activeBool
    while True:
        if not activeBool:
            if listenKeyWord():
                activeBool = True
                tts.welcome()
        else:
            action = listen()

            if 'prueba de sonido' in action: # Performs a sound test
                activeBool = tts.soundTest()
            elif 'reproduce' in action or ('pon' in action and 'alarma' not in action): # Plays a song request by user via youtube
                print()
            elif 'pon' in action and 'alarma' in action: # Set an alarm
                print()
            elif ('tiempo hace' in action or 'clima hace') and 'en' not in action: # Get the actual user place weather
                print()
            elif ('tiempo hace' in action or 'clima hace') and 'en' in action: # Get the place weather given by user
                print()
            elif 'hora es' in action and 'en' not in action: # Get the actual time of the user
                print()
            elif 'hora es' in action and 'en' not in action: # Get the actual time of a zone given by user
                print()
            elif ('sube' in action or 'subir' in action) and 'volumen' in action: # Turn volume up
                print()
            elif ('baja' in action or 'bajar' in action) and 'volumen' in action: # Turn volume down
                print()
            elif 'hasta luego' in action: # Close app
                tts.goodbye()
                activeModel.set() # Send an advise to the Kivy's Interface Thread to close the app