from tasks import open_app, web_search
from speech_engine import speak

def process(command):
    print(f"Command received: {command}")

    if "open" in command:
        open_app.launch(command)
    elif "search" in command:
        web_search.search(command)
        return None
    else:
        speak("I didn't understand the command.")
        print(" Unmatched command.")
        return None