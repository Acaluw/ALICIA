# pip install pycaw
import platform
import subprocess
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Get actual os
def getOs():
    pltName = platform.system().lower()

    if 'windows' in pltName:
        return 'windows'
    elif 'linux' in pltName:
        return 'linux'
    else:
        return 'windows' # Default platform in develop time

# Update system actual value
def set_volume(level):
    os = getOs()

    while level >= 100:
        level = round(level/10)

    if os == 'windows':
        volume = level * 10  # Convert value in a scale of 1 to 10

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_control = cast(interface, POINTER(IAudioEndpointVolume))

        # -65.25 minimum value // 0.0 maximum value
        # Convert volume (0-100) in a value of that range
        newVol = volume / 100 * (0.0 + 65.25) - 65.25
        volume_control.SetMasterVolumeLevel(newVol, None)
    elif os == 'linux':
        volume = level * 10  # Convert value in a scale of 1 to 10
        command = ["amixer", "sset", "'Master'", f"{volume}%"]
        subprocess.run(command)
    
if __name__ == '__main__':
    os = getOs()
    print(os)
    set_volume(5)