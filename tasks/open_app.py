import os
import subprocess
from speech_engine import speak

def launch(command):
    print(f" Launching: {command}")

    if "notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")

    elif "calculator" in command or "calc" in command:
        speak("Opening Calculator.")
        os.system("calc")

    elif "chrome" in command:
        speak("Opening Google Chrome.")
        os.system("start chrome")

    elif "paint" in command:
        speak("Opening Paint.")
        os.system("mspaint")

    elif "command prompt" in command or "cmd" in command:
        speak("Opening Command Prompt.")
        os.system("start cmd")

    elif "task manager" in command:
        speak("Opening Task Manager.")
        os.system("taskmgr")

    elif "file explorer" in command or "explorer" in command:
        speak("Opening File Explorer.")
        os.system("explorer")

    elif "control panel" in command:
        speak("Opening Control Panel.")
        os.system("control")

    elif "word" in command:
        speak("Opening Microsoft Word.")
        subprocess.Popen(["start", "winword"], shell=True)

    elif "excel" in command:
        speak("Opening Microsoft Excel.")
        subprocess.Popen(["start", "excel"], shell=True)

    elif "powerpoint" in command:
        speak("Opening Microsoft PowerPoint.")
        subprocess.Popen(["start", "powerpnt"], shell=True)

    elif "edge" in command:
        speak("Opening Microsoft Edge.")
        os.system("start msedge")

    elif "firefox" in command:
        speak("Opening Mozilla Firefox.")
        os.system("start firefox")

    elif "youtube" in command:
        speak("Opening YouTube.")
        os.system("start https://www.youtube.com")

    elif "spotify" in command:
        speak("Opening Spotify.")
        os.startfile("C:\\Users\\YourUsername\\AppData\\Roaming\\Spotify\\Spotify.exe")  

    elif "vscode" in command or "visual studio code" in command or "code editor" in command:
        speak("Opening Visual Studio Code.")
        os.system("code")

    elif "discord" in command:
        speak("Opening Discord.")
        os.startfile("C:\\Users\\asus\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")  

    elif "zoom" in command:
        speak("Opening Zoom.")
        os.startfile("C:\\Users\\asus\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

    elif "powershell" in command:
        speak("Opening PowerShell.")
        os.system("start powershell")

    elif "device manager" in command:
        speak("Opening Device Manager.")
        os.system("devmgmt.msc")

    elif "services" in command:
        speak("Opening Services.")
        os.system("services.msc")

    elif "registry editor" in command:
        speak("Opening Registry Editor.")
        os.system("regedit")

    elif "snipping tool" in command or "screenshot" in command:
        speak("Opening Snipping Tool.")
        os.system("snippingtool")

    elif "windows security" in command or "antivirus" in command:
        speak("Opening Windows Security.")
        os.system("start windowsdefender:")

    elif "event viewer" in command:
        speak("Opening Event Viewer.")
        os.system("eventvwr")

    elif "windows update" in command:
        speak("Opening Windows Update settings.")
        os.system("start ms-settings:windowsupdate")

    elif "system information" in command:
        speak("Opening System Information.")
        os.system("msinfo32")

    elif "camera" in command:
        speak("Opening Camera.")
        os.system("start microsoft.windows.camera:")

    elif "calculator" in command:
        speak("Opening Calculator.")
        os.system("calc")

    elif "notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")
    else:
        speak("Sorry, I don't recognize that application.")
        print(" Unknown app.")
        

