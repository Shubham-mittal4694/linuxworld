#!/usr/bin/env python3

import cgi
import cgitb
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers including CORS headers
print("Content-Type: text/plain")
print("Access-Control-Allow-Origin: *")  # Allow requests from any origin (you can restrict it as needed)
print()  # Blank line required between headers and body

def get_system_volume():
    try:
        # Get default audio endpoint (speakers)
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        
        # Retrieve current system volume level
        current_volume = volume_interface.GetMasterVolumeLevelScalar() * 100
        return f"Current system volume: {current_volume}%"
    except Exception as e:
        return f"Failed to retrieve volume: {str(e)}"

def set_system_volume(volume_level):
    try:
        # Get default audio endpoint (speakers)
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        
        # Set the system volume to the specified level
        volume_interface.SetMasterVolumeLevelScalar(volume_level / 100.0, None)
        return f"System volume set to {volume_level}%"
    except Exception as e:
        return f"Failed to set volume: {str(e)}"

def main():
    form = cgi.FieldStorage()

    if "volume" in form:
        try:
            user_volume = float(form.getvalue("volume"))
            if 0 <= user_volume <= 100:
                result = set_system_volume(user_volume)
            else:
                result = "Please enter a value between 0 and 100."
        except ValueError:
            result = "Invalid input. Please enter a numerical value between 0 and 100."
    else:
        result = get_system_volume()

    print(result)

if __name__ == "__main__":
    main()
