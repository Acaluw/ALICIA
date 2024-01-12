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

            if 'prueba de sonido' in action:
                activeBool = tts.soundTest()
            elif 'cancion' in action or 'canción' in action:
                activeBool = tts.cancion()
            elif 'hasta luego' in action:
                tts.goodbye()
                activeModel.set()