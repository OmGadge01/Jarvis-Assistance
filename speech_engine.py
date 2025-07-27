import speech_recognition as sr
import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 180)

speak_lock = threading.Lock()

def speak(text):
    def _speak():
        with speak_lock:
            print(f"Jarvis: {text}")
            engine.say(text)
            engine.runAndWait()

    threading.Thread(target=_speak).start()


def listen(stop_event=None):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

            if stop_event and stop_event.is_set():
                print("Listening stopped externally.")
                return None

            print("Audio captured. Recognizing...")
            speak("Audio captured. Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google; {e}")
            speak("Speech service is unavailable.")
            return None
        except Exception as e:
            print(f"Error during listening: {e}")
            speak("Something went wrong.")
            return None
