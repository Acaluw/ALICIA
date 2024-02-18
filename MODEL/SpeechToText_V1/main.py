# pip install SpeechRecognition

# Libs import
import sys
import time
from threading import Event
from pathlib import Path
import speech_recognition as sr

# Making TextToSpeech/main.py visible for this file
root_path = Path(__file__).resolve().parents[1]
sys.path.append(str(root_path))
from TextToSpeech_V1 import main as tts

# Main Variables
voiceRecog = sr.Recognizer()
activeBool = False
camCapture = False
camCaptureChanged = Event()

# Method that listen for a keyword to activate listen() method
def listenKeyWord():
    with sr.Microphone() as source:
        print("SpeechToText || Waiting for keyword")
        voiceRecog.adjust_for_ambient_noise(source, duration=1)
        audio = voiceRecog.listen(source)

    try:
        texto = voiceRecog.recognize_google(audio, language='es')
        print(f'SpeechToText || Keyword: {texto}')
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
    while True:
        if not activeBool:
            if listenKeyWord():
                activeBool = True
                tts.welcome()
        else:
            action = listen()
            print(f'SpeechToText || Action: {action}')
            if 'prueba de sonido' in action: # Performs a sound test
                activeBool = tts.soundTest()
            elif 'hora es' in action: # Get the actual time of the user
                activeBool = tts.ActualTime()
            elif 'día es hoy' in action: # Get the actual day
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
            elif 'hasta luego' in action: # Close app
                tts.goodbye()
                # Close Tkinter gui

if __name__ == '__main__':
    print('+------------------------------------+')
    print('|  ALICIA v1.0                       |')
    print('+------------------------------------+')
    runSpeechModel()