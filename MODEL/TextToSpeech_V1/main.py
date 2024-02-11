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
    print('TextToSpeech || SoundTest')
    engine.say(lang.esp['test'])
    engine.runAndWait()
    engine.stop()
    return False

def welcome():
    engine.say(lang.esp['welcome'])
    engine.runAndWait()

def ActualTime():
    print('TextToSpeech || ActualTime')
    acTime = time.getActualTime()
    engine.say(acTime)
    engine.runAndWait()
    return False

def ActualDay():
    print('TextToSpeech || ActualDay')
    acDay = time.getActualDay()
    engine.say(acDay)
    engine.runAndWait()
    return False

def SetVolume(value):
    print(f'TextToSpeech || SetVolume ({value})')
    volumeControl.set_volume(value)
    return False

def playAudio(name):
    print(f'TextToSpeech || PlayAudio ({name})')
    engine.say(f'Reproduciendo {name}')
    engine.runAndWait()
    audioPath = soundmusic.audioDownload(name)
    soundmusic.audioPlay(audioPath)
    return False

def stopAudio():
    print(f'TextToSpeech || StopAudio')
    soundmusic.audioStop()
    return False

def pauseAudio():
    print(f'TextToSpeech || PauseAudio')
    soundmusic.audioPause()
    return False

def resumeAudio():
    print(f'TextToSpeech || ResumeAudio')
    soundmusic.audioResume()
    return False

def goodbye():
    print('TextToSpeech || Goodbye')
    engine.say(lang.esp['goodbye'])
    engine.runAndWait()

def cancion():
    engine.say('Reproduciendo temazo...')
    engine.runAndWait()
    return False

if __name__ == "__main__":
    soundTest()