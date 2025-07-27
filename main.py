import eel
from speech_engine import listen, speak
from command_processor import process
import threading
import time

eel.init('gui')

jarvis_running = False
stop_event = threading.Event()
def run_jarvis():
    global jarvis_running
    jarvis_running = True
    stop_event.clear()
    
    while jarvis_running and not stop_event.is_set():
        command = listen(stop_event=stop_event)
        if command:
            process(command)
        time.sleep(1)


@eel.expose
def start_jarvis():
    threading.Thread(target=run_jarvis).start()


@eel.expose
def stopJarvis():
    global jarvis_running
    jarvis_running = False
    stop_event.set()  


eel.start('index.html', size=(500, 600))
