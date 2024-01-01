import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def soundTest():
    text = "Esta es una prueba de sonido"
    engine.say(text)
    engine.runAndWait()
    engine.stop()


if __name__ == "__main__":
    soundTest()