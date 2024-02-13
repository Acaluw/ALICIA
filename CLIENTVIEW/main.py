#python -m pip install --upgrade pip wheel setuptools
#python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
#python -m pip install kivy.deps.gstreamer
#pip install kivy
#pip install pylance
#pip install Pillow

import sys
import cv2 as cv
import numpy as np
import threading
from kivy.app import App
from kivy.clock import Clock
from pathlib import Path
from PIL import Image

# Making SpeechToText_V1/main.py visible for this file
root_path = Path(__file__).resolve().parents[1]
sys.path.append(str(root_path))
from MODEL.SpeechToText_V1 import main as stt

class Alicia(App):
    # Start Client Interface
    def build(self):
        self.title = 'Alicia v.0.0.3'
        self.SpeechToText_Thread()
        self.activeWindow = stt.activeModel
        Clock.schedule_interval(self.checkActiveWindow, 1)
    
    # Start SpeechToText model in a separated Thread
    def SpeechToText_Thread(self):
        speechThread = threading.Thread(target=stt.runSpeechModel)
        speechThread.daemon = True # True -> Close Thread when closing the client window
        speechThread.start()

    # Method that check if the window will still open
    def checkActiveWindow(self, dt):
        if self.activeWindow.is_set():
            self.stop()
            return False
    
    # Methods that get an image capture from the camera
    def cameraImgCapture(self):
        camera = self.root.ids.cam
        texture = camera.texture
        size = texture.size
        pixels = texture.pixels

        pilImg=Image.frombytes(mode='RGBA', size=size,data=pixels) # Create PIL Image from Kivy data
        numpypicture=np.array(pilImg) # Convert PIL Image to a numpy array
        numpypicture = cv.cvtColor(numpypicture, cv.COLOR_RGBA2BGR) # Pass Image RGBA to opencv BGR
        cv.imwrite("TEMPFILES/images/productImg.png", numpypicture) # Save image in image folder


if __name__ == '__main__':
    Alicia().run()