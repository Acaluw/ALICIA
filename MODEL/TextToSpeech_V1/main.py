# pip install pyttsx3
import sys
from pathlib import Path
import pyttsx3
import logging

logging.basicConfig(level=logging.INFO, filename="TEMPFILES/mainLog.log",filemode="w")

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
        logging.info("TextToSpeech || SoundTest")
        engine.say(lang.esp['test'])
        engine.runAndWait()
        engine.stop()
        return False
    except:
        logging.error("TextToSpeech || SoundTest: Comando no disponible")
        return False

def welcome():
    engine.say(lang.esp['welcome'])
    engine.runAndWait()

def ActualTime():
    try:
        print('TextToSpeech || ActualTime')
        logging.info("TextToSpeech || ActualTime")
        acTime = time.getActualTime()
        engine.say(acTime)
        engine.runAndWait()
        return False
    except:
        logging.error("TextToSpeech || ActualTime: Comando no disponible")
        return False

def ActualDay():
    try:
        print('TextToSpeech || ActualDay')
        logging.info("TextToSpeech || ActualDay")
        acDay = time.getActualDay()
        engine.say(acDay)
        engine.runAndWait()
        return False
    except:
        logging.error("TextToSpeech || ActualDay: Comando no disponible")
        return False

def SetVolume(value):
    try:
        print(f'TextToSpeech || SetVolume ({value})')
        logging.info(f"TextToSpeech || SetVolume ({value})")
        volumeControl.set_volume(value)
        return False
    except:
        logging.error("TextToSpeech || SetVolume: Comando no disponible")
        return False

def playAudio(name):
    try:
        print(f'TextToSpeech || PlayAudio ({name})')
        logging.info(f"TextToSpeech || PlayAudio ({name})")
        engine.say(f'Reproduciendo {name}')
        engine.runAndWait()
        audioPath = soundmusic.audioDownload(name)
        soundmusic.audioPlay(audioPath)
        return False
    except:
        logging.error("TextToSpeech || PlayAudio: Comando no disponible")
        return False

def stopAudio():
    try:
        print(f'TextToSpeech || StopAudio')
        logging.info("TextToSpeech || StopAudio")
        soundmusic.audioStop()
        return False
    except:
        logging.error("TextToSpeech || StopAudio: Comando no disponible")
        return False

def pauseAudio():
    try:
        print(f'TextToSpeech || PauseAudio')
        logging.info("TextToSpeech || PauseAudio")
        soundmusic.audioPause()
        return False
    except:
        logging.error("TextToSpeech || PauseAudio: Comando no disponible")
        return False

def resumeAudio():
    try:
        print(f'TextToSpeech || ResumeAudio')
        logging.info("TextToSpeech || ResumeAudio")
        soundmusic.audioResume()
        return False
    except:
        logging.error("TextToSpeech || ResumeAudio: Comando no disponible")
        return False

def goodbye():
    try:
        print('TextToSpeech || Goodbye')
        logging.info("TextToSpeech || Goodbye")
        engine.say(lang.esp['goodbye'])
        engine.runAndWait()
    except:
        logging.error("TextToSpeech || Goodbye: Comando no disponible")
        return False

if __name__ == "__main__":
    soundTest()