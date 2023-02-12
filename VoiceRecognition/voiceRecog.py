import subprocess
from modules import speech_recognition
from app import mainApp


class voiceRecogClass:
    
    def voice_recognizing():
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.1)
            audio = recognizer.listen(mic)
        try:
            text = recognizer.recognize_google(audio).lower()
            return text
        except speech_recognition.UnknownValueError:
            return ""

    def find_app_from_voice(app_input):
        if "notepad" in app_input:
                subprocess.Popen(mainApp.app_map["notepad"])
        elif "calculator" in app_input or "calc" in app_input:
            subprocess.Popen(mainApp.app_map["calculator"])
        elif "paint" in app_input:
            subprocess.Popen(mainApp.app_map["paint"])
        elif "chrome" in app_input or "browser" in app_input:
            if mainApp.app_map["chrome"]:
                subprocess.Popen(mainApp.app_map["chrome"])
            else:
                print("Google Chrome not found.")
        # elif find_app(app_input) == True:
        #     run_app(find_app(app_input))
        # if find_app(app_input) == True:
        #     run_app(find_app(app_input))
        # elif "exit" in app_input:
        #     os._exit(0)
        else:
            print("Application not found. Please try again.")