#python -m pip install --upgrade pip wheel setuptools
#python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
#python -m pip install kivy.deps.gstreamer
#pip install kivy

from kivy.app import App
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.graphics.texture import Texture
from pathlib import Path
from io import BytesIO
import threading
import sys
import os

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
        
    # Method that get an image capture from the camera
    def cameraImageCapture(self):
        camera = self.root.ids.cam
        texture = camera.texture


if __name__ == '__main__':
    Alicia().run()