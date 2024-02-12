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
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

def welcome():
    engine.say(lang.esp['welcome'])
    engine.runAndWait()

def ActualTime():
    try:
        print('TextToSpeech || ActualTime')
        acTime = time.getActualTime()
        engine.say(acTime)
        engine.runAndWait()
        return False
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

def ActualDay():
    try:
        print('TextToSpeech || ActualDay')
        acDay = time.getActualDay()
        engine.say(acDay)
        engine.runAndWait()
        return False
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

def SetVolume(value):
    try:
        print(f'TextToSpeech || SetVolume ({value})')
        volumeControl.set_volume(value)
        return False
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

def playAudio(name):
    try:
        print(f'TextToSpeech || PlayAudio ({name})')
        engine.say(f'Reproduciendo {name}')
        engine.runAndWait()
        audioPath = soundmusic.audioDownload(name)
        soundmusic.audioPlay(audioPath)
        return False
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

def stopAudio():
    try:
        print(f'TextToSpeech || StopAudio')
        soundmusic.audioStop()
        return False
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

def pauseAudio():
    try:
        print(f'TextToSpeech || PauseAudio')
        soundmusic.audioPause()
        return False
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

def resumeAudio():
    try:
        print(f'TextToSpeech || ResumeAudio')
        soundmusic.audioResume()
        return False
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

def goodbye():
    try:
        print('TextToSpeech || Goodbye')
        engine.say(lang.esp['goodbye'])
        engine.runAndWait()
    except:
        engine.say('Comando no disponible')
        engine.runAndWait()
        engine.stop()
        return False

if __name__ == "__main__":
    soundTest()