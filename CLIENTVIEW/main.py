#python -m pip install --upgrade pip wheel setuptools
#python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
#python -m pip install kivy.deps.gstreamer
#pip install kivy
from kivy.app import App

class Alicia(App):
    def build(self):
        self.title = 'Alicia v.0.0.1'


if __name__ == '__main__':
    Alicia().run()