import sys
from pathlib import Path
import pyttsx3

import simpleaudio

root_path = Path(__file__).resolve().parents[2]
sys.path.append(str(root_path))
from LANGUAGES import main as lang

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def soundTest():
    engine.say(lang.esp['test'])
    engine.runAndWait()
    engine.stop()
    return False

def welcome():
    engine.say(lang.esp['welcome'])
    engine.runAndWait()

def timeCheck(time):
    engine.say(lang.esp['timeCheck']+time)
    engine.runAndWait()

def cancion():
    engine.say('Reproduciendo temazo...')
    engine.runAndWait()
    # audio = simpleaudio.WaveObject.from_wave_file('C:\\Users\\Juan\\Documents\\GitHub\\ALICIA\\MODEL\\TextToSpeech_V1\\si.wav')
    # playAudio = audio.play()
    # playAudio.wait_done()
    return False

if __name__ == "__main__":
    soundTest()