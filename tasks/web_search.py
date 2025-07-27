import webbrowser
from speech_engine import speak

def search(command):
    speak("Searching the web.")
    query = command.replace("search", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")
