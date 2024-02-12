# pip install pytube
# pip install python-vlc
from pytube import YouTube
from pytube import Search
import threading
import time
import vlc

player = None
thread = None

def audioDownload(name):

    if 'lyrics' not in name and 'letra' not in name:
        name = name+' letra'
    
    s = Search(name) # Performs a youtube search
    for video in s.results:
        url = video.watch_url # Take first result
        break
    
    # Download audio
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    fileDownload = stream.download(output_path='TEMPFILES', filename='reproTemp')

    return fileDownload

def audioPlay(filePath):
    global thread
    def play():
        print(f'Sound&Music || PATH: {filePath}')
        # Play audio
        global player
        player = vlc.MediaPlayer(filePath)
        player.play()

        # Wait till audio finish
        while player.get_state() != vlc.State.Playing:
            time.sleep(0.1)
        
        audioLength = player.get_length() / 1000
        print(f'Sound&Music || Music Length: {audioLength}')
        time.sleep(audioLength)
    thread = threading.Thread(target=play)
    thread.start()

def audioPause():
    if player:
        player.pause()

def audioResume():
    if player:
        player.play()

def audioStop():
    if player:
        player.stop()
    
if __name__ == '__main__':
    testName = input('video search test: ')
    audioPath = audioDownload(testName)
    audioPlay(audioPath)
    threadTest = input('Thread Test: ')
    if (threadTest == 'stop'): audioStop()