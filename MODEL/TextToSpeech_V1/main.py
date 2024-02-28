# pip install pyttsx3
import sys
from pathlib import Path
import pyttsx3

# Documentation: https://pyttsx3.readthedocs.io/en/latest/

root_path = Path(__file__).resolve().parents[2]
sys.path.append(str(root_path))
from METHODS.Time import time
from METHODS.VolumeControl import volumeControl
from METHODS.SoundMusic import soundmusic
from METHODS.QRcode import qrcode
from METHODS.GoogleSearch import googleSearch as gs
from METHODS.FindPlaces import findPlaces
from METHODS.CapitalCountry import capital_country
from METHODS.Weather import weatherMethod

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# soundTest() -> Plays default message to test the engine
def soundTest():
    try:
        print('TextToSpeech || SoundTest')
        engine.say("Esta es una prueba de sonido")
        engine.runAndWait()
        engine.stop()
        return False
    except Exception:
        print(f"TextToSpeech || SoundTest: {Exception}")
        return False

# welcome() -> Perform a welcome message when the keyword is detected
def welcome():
    try:
        print('TextToSpeech || Welcome')
        engine.say("¿En qué puedo ayudarte?")
        engine.runAndWait()
    except Exception:
        print(f"TextToSpeech || Welcome: {Exception}")

# ActualTime(input: string) -> Get time based on input value
def ActualTime(input=""):
    try:
        print('TextToSpeech || ActualTime')
        if input == "":
            acTime = time.getActualTime()
        else:
            acTime = time.getHour(input)
        engine.say(acTime)
        engine.runAndWait()
        return False
    except Exception:
        print(f"TextToSpeech || ActualTime: {Exception}")
        return False

# ActualDay() -> Get the actual day
def ActualDay():
    try:
        print('TextToSpeech || ActualDay')
        acDay = time.getActualDay()
        engine.say(acDay)
        engine.runAndWait()
        return False
    except Exception:
        print(f"TextToSpeech || ActualDay: {Exception}")
        return False

# SetVolume(value: number) -> Change system volume
def SetVolume(value):
    try:
        print(f'TextToSpeech || SetVolume ({value})')
        volumeControl.set_volume(value)
        return False
    except Exception:
        print(f"TextToSpeech || SetVolume: {Exception}")
        return False

# playAudio(name: string) -> Search in youtube the name variable audio to play it
def playAudio(name):
    try:
        print(f'TextToSpeech || PlayAudio ({name})')
        engine.say(f'Reproduciendo {name}')
        engine.runAndWait()
        audioPath = soundmusic.audioDownload(name)
        soundmusic.audioPlay(audioPath)
        return False
    except Exception:
        print(f"TextToSpeech || PlayAudio: {Exception}")
        return False

# stopAudio() -> Stop actual song
def stopAudio():
    try:
        print(f'TextToSpeech || StopAudio')
        soundmusic.audioStop()
        return False
    except Exception:
        print(f"TextToSpeech || StopAudio: {Exception}")
        return False

# pauseAudio() -> Pause actual song
def pauseAudio():
    try:
        print(f'TextToSpeech || PauseAudio')
        soundmusic.audioPause()
        return False
    except Exception:
        print(f"TextToSpeech || PauseAudio: {Exception}")
        return False

# resumeAudio() -> Resume actual song
def resumeAudio():
    try:
        print(f'TextToSpeech || ResumeAudio')
        soundmusic.audioResume()
        return False
    except Exception:
        print(f"TextToSpeech || ResumeAudio: {Exception}")
        return False

# getQrCode() -> Scan QRCode from the gui's webcam
def getQrCode():
    try:
        print(f'TextToSpeech || GetQrCode')
        engine.say("Aquí tienes el contenido del código qr")
        engine.runAndWait()
        qrcode.qrSearch()
        return False
    except Exception:
        print(f"TextToSpeech || GetQrCode: {Exception}")
        return False

# googleSearch(key: string) -> Search in google for the best option for the key value
def googleSearch(key):
    try:
        print(f'TextToSpeech || GoogleSearch')
        searchRequest = key.split("busca")[1].strip()
        engine.say(f"Buscando la solicitud: {searchRequest}")
        engine.runAndWait()
        gs.googleSearch(searchRequest)
        return False
    except Exception:
        print(f"TextToSpeech || GoogleSearch: {Exception}")
        return False

# findPlace(zone: string, type: string) -> Search nearby type's value in a specific range in zone's value
def findPlace(zone, type):
    try:
        print(f'TextToSpeech || FindPlace {zone}/{type}')
        engine.say(f"Buscando {type} cercanos en {zone}")
        engine.runAndWait()
        lat, long = findPlaces.obtener_latitud_longitud(zone)
        findPlaces.buscar_place_cercanos(latitud=lat, longitud=long, tipo=type)
        return False
    except Exception:
        print(f"TextToSpeech || FindPlace: {Exception}")
        return False

# capitalCountry(country: string) -> Gives the actual country of the country's variable input
def capitalCountry(country):
    try:
        print(f'TextToSpeech || CapitalCountry')
        engine.say(f"Buscando la capital de {country}")
        engine.runAndWait()
        res = capital_country.obtener_capital(country)
        engine.say(f"La capital de {country} es: {res}")
        engine.runAndWait()
        return False
    except Exception:
        print(f"TextToSpeech || CapitalCountry: {Exception}")
        return False

# weatherControl(input: string) -> Get actual weather of the places's input value    
def weatherControl(input):
    try:
        print(f'TextToSpeech || WeatherControl')
        res = weatherMethod.obtener_clima(input)
        engine.say(res)
        engine.runAndWait()
        return False
    except Exception:
        print(f"TextToSpeech || WeatherControl: {Exception}")
        return False

# notFound() -> Call it when no available action is request by user
def notFound():
    try:
        print(f'TextToSpeech || NotFound')
        engine.say(f"Perdona, no te he entendido")
        engine.runAndWait()
    except Exception:
        print(f"TextToSpeech || NotFound: {Exception}")
        return False

# goodbye() -> Performs a goodbye message
def goodbye():
    try:
        print('TextToSpeech || Goodbye')
        engine.say("¡Hasta pronto!")
        engine.runAndWait()
    except Exception:
        print(f"TextToSpeech || Goodbye: {Exception}")
        return False

if __name__ == "__main__":
    soundTest()