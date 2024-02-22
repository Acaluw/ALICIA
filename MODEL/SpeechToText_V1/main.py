# pip install SpeechRecognition

# Libs import
import sys
from threading import Event
from pathlib import Path
import speech_recognition as sr
import os
from xml.etree import ElementTree as ET
from datetime import datetime
import socket

# Documentation: https://pypi.org/project/SpeechRecognition/
# https://realpython.com/python-speech-recognition/

# Making TextToSpeech/main.py visible for this file
root_path = Path(__file__).resolve().parents[1]
sys.path.append(str(root_path))
from TextToSpeech_V1 import main as tts

# Main Variables
voiceRecog = sr.Recognizer()
activeBool = False
camCapture = False
speechStatus = ""
guiStatus = True
logMessage = ""
camCaptureChanged = Event()
speechStatusChanged = Event()
guiStatusChanged = Event()
logMessageChanged = Event()

# Method that listen for a keyword to activate listen() method
def listenKeyWord():
    global speechStatus
    global logMessage
    with sr.Microphone() as source:
        print("SpeechToText || Waiting for keyword")
        speechStatus = "Waiting"
        speechStatusChanged.set()
        voiceRecog.adjust_for_ambient_noise(source, duration=1)
        audio = voiceRecog.listen(source)

    try:
        texto = voiceRecog.recognize_google(audio, language='es')
        print(f'SpeechToText || Keyword: {texto}')
        logMessage = texto
        logMessageChanged.set()
        if 'Alicia' in texto:
            return True
    except sr.UnknownValueError:
        return False

# Method that listen for a current command
def listen():
    with sr.Microphone() as source:
        print("SpeechToText || Command section...")
        voiceRecog.adjust_for_ambient_noise(source, duration=1)
        audio = voiceRecog.listen(source)

    try:
        texto = voiceRecog.recognize_google(audio,language='es')
        print("SpeechToText || Command detected...")
        return texto.lower()
    except sr.UnknownValueError:
        return ""
    
# Active loop that keep listening for the keyword
def runSpeechModel():
    global activeBool
    global camCapture
    global speechStatus
    global guiStatus
    global logMessage

    # THIS VARIABLE IS ONLY TO TEST METADATA XML GENERATION !!!!
    ip_address = socket.gethostbyname(socket.gethostname()) # Gets user ip
    if not os.path.exists('TEMPFILES/log.xml'):
        os.makedirs(os.path.dirname('TEMPFILES/log.xml'), exist_ok=True) # Create the directory if it does not exist
        root = ET.Element("root") # Create the root element
        tree = ET.ElementTree(root)
        tree.write('TEMPFILES/log.xml')
    else:
        tree = ET.parse('TEMPFILES/log.xml') # Load the existing XML file
        root = tree.getroot()

    accion = ET.SubElement(root, "sessionlog")
    accion.set("ip", ip_address)
    fecha = ET.SubElement(accion, "fecha")
    fecha.text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    while True:
        if not activeBool:
            if listenKeyWord():
                activeBool = True
                tts.welcome()
                speechStatus = "Listening"
                speechStatusChanged.set()
        else:
            action = listen()
            print(f'SpeechToText || Action: {action}')
            comando = ET.SubElement(accion, "comando")
            comando.text = action
            tree.write('TEMPFILES/log.xml')
            logMessage = action
            logMessageChanged.set()
            if 'prueba de sonido' in action: # Performs a sound test
                activeBool = tts.soundTest()
            elif 'hora es' in action: # Get current time of the user
                activeBool = tts.ActualTime()
            elif 'hora es' in action and 'en' in action: # Get current time of the place given by user
                activeBool = tts.ActualTime(action)
            elif 'día es hoy' in action: # Get current day
                activeBool = tts.ActualDay()
            elif ('volumen' in action or 'Volumen' in action) and 'al' in action: # Change volume value
                volValue = int(action.split('al')[1].strip())
                activeBool = tts.SetVolume(volValue)
            elif 'reproduce' in action or 'pon' in action: # Play a song given by user
                songName = ''
                if 'reproduce' in action:
                    songName = action.split('reproduce')[1].strip()
                elif 'pon' in action:
                    songName = action.split('reproduce')[1].strip()
                activeBool = tts.playAudio(songName)
            elif ('para' in action or 'quita' in action) and 'canción' in action: # Stop actual song
                activeBool = tts.stopAudio()
            elif 'pausa' in action: # Pause actual song
                activeBool = tts.pauseAudio()
            elif 'continua' in action or 'reanuda' in action: # Resume actual song
                activeBool = tts.resumeAudio()
            elif ('escanea' in action or 'busca' in action) and 'código' in action: # Search for Qr Code in cam
                camCapture = True
                camCaptureChanged.set()
                camCapture = False
                activeBool = tts.getQrCode()
            elif 'busca' in action: # Search product via voice request
                activeBool = tts.googleSearch(action.lower())
            elif ('encuentra' in action) and ('cercanos en' in action or ('en' in action and 'cercanos' not in action) or 'por' in action): # Search nearby places
                if 'cercanos en' in action:
                    petiSt = action.split('encuentra')[1].split("cercanos")[0].strip()
                    petiSt2 = action.split('cercanos en')[1].strip()
                    activeBool = tts.findPlace(zone=petiSt2, type=petiSt)
                elif 'cercanos por' in action:
                    petiSt = action.split('encuentra')[1].split("cercanos")[0].strip()
                    petiSt2 = action.split('cercanos por')[1].strip()
                    print(f'tipo {petiSt} y zona {petiSt2}')
                    activeBool = tts.findPlace(zone=petiSt2, type=petiSt)
            elif ('tiempo' in action or 'clima' in action) and 'en' in action: # Gets weather of a place specified by user (only country)
                 activeBool = tts.weatherControl(action)
            elif 'capital' in action and 'de' in action: # Gets country's capital
                 petiSt = action.find('de')
                 country = action.split("de")[1].strip()
                 activeBool = tts.capitalCountry(country=country)
            elif 'hasta luego' in action: # Close app
                tts.goodbye()
                guiStatus = False
                guiStatusChanged.set() # Close Tkinter gui
            else:
                activeBool = tts.notFound()

if __name__ == '__main__':
    print('+------------------------------------+')
    print('|  ALICIA v1.0                       |')
    print('+------------------------------------+')
    runSpeechModel()