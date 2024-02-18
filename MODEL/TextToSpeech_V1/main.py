# pip install pyttsx3
import sys
from pathlib import Path
import pyttsx3

root_path = Path(__file__).resolve().parents[2]
sys.path.append(str(root_path))
from LANGUAGES import main as lang
from METHODS.Time import time
from METHODS.VolumeControl import volumeControl
from METHODS.SoundMusic import soundmusic
from METHODS.QRcode import qrcode
from METHODS.GoogleSearch import googleSearch as gs

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def soundTest():
    try:
        print('TextToSpeech || SoundTest')
        engine.say(lang.esp['test'])
        engine.runAndWait()
        engine.stop()
        return False
    except Exception:
        print(f"TextToSpeech || SoundTest: {Exception}")
        return False

def welcome():
    try:
        print('TextToSpeech || Welcome')
        engine.say(lang.esp['welcome'])
        engine.runAndWait()
    except Exception:
        print(f"TextToSpeech || Welcome: {Exception}")

def ActualTime():
    try:
        print('TextToSpeech || ActualTime')
        acTime = time.getActualTime()
        engine.say(acTime)
        engine.runAndWait()
        return False
    except Exception:
        print(f"TextToSpeech || ActualTime: {Exception}")
        return False

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

def SetVolume(value):
    try:
        print(f'TextToSpeech || SetVolume ({value})')
        volumeControl.set_volume(value)
        return False
    except Exception:
        print(f"TextToSpeech || SetVolume: {Exception}")
        return False

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

def stopAudio():
    try:
        print(f'TextToSpeech || StopAudio')
        soundmusic.audioStop()
        return False
    except Exception:
        print(f"TextToSpeech || StopAudio: {Exception}")
        return False

def pauseAudio():
    try:
        print(f'TextToSpeech || PauseAudio')
        soundmusic.audioPause()
        return False
    except Exception:
        print(f"TextToSpeech || PauseAudio: {Exception}")
        return False

def resumeAudio():
    try:
        print(f'TextToSpeech || ResumeAudio')
        soundmusic.audioResume()
        return False
    except Exception:
        print(f"TextToSpeech || ResumeAudio: {Exception}")
        return False

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

def googleSearch(key):
    try:
        print(f'TextToSpeech || GoogleSearch')
        searchRequest = key.split("busca")[1].strip()
        engine.say(f"Buscando la solicitud: {searchRequest}")
        engine.runAndWait()
        gs.googleSearch(searchRequest)
    except Exception:
        print(f"TextToSpeech || GoogleSearch: {Exception}")
        return False
    
def notFound():
    try:
        print(f'TextToSpeech || NotFound')
        engine.say(f"Perdona, no te he entendido")
        engine.runAndWait()
    except Exception:
        print(f"TextToSpeech || NotFound: {Exception}")
        return False

def goodbye():
    try:
        print('TextToSpeech || Goodbye')
        engine.say(lang.esp['goodbye'])
        engine.runAndWait()
    except Exception:
        print(f"TextToSpeech || Goodbye: {Exception}")
        return False

if __name__ == "__main__":
    soundTest()