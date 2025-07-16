import webbrowser
import music_library  
from speak import speak

def play_song(command):
    song = " ".join(command.lower().split(" ")[1:])
    try:
        link = music_library.music[song]
        webbrowser.open(link)
    except KeyError:
        speak(f"Sorry, the song '{song}' was not found in your library.")
