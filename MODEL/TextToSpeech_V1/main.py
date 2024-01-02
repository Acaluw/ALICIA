import pyttsx3
from LANGUAGES import main as lg

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def soundTest():
    engine.say(lg.esp['test'])
    engine.runAndWait()
    engine.stop()

def welcome():
    engine.say(lg.esp['welcome'])
    engine.runAndWait()

def timeCheck(time):
    engine.say(lg.esp['timeCheck']+time)
    engine.runAndWait()

if __name__ == "__main__":
    soundTest()