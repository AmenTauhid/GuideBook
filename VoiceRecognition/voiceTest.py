# import speech_recognition
# import pyttsx3
# import subprocess
# import winreg
# import platform
# import app
# import os


# def voice_recognizing():
#     recognizer = speech_recognition.Recognizer() 
#     while True:
#         try:
#             with speech_recognition.Microphone() as mic:
#                 recognizer.adjust_for_ambient_noise(mic,duration= 0.1)
#                 audio = recognizer.listen(mic)
#                 text = recognizer.recognize_google(audio)
#                 text = text.lower()
#                 return str(text)
#                 print(f"Recognized {text}")
            
                

#         except speech_recognition.UnknownValueError():
#             recognizer = speech_recognition.Recognizer()
#             continue

# def find_chrome():
#     try:
#         reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
#         key = winreg.OpenKey(reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe")
#         path = winreg.QueryValue(key, None)
#         winreg.CloseKey(key)
#         return path
#     except WindowsError:
#         return None

# app_map = {
#     "notepad": ["notepad.exe"],
#     "calculator": ["calc.exe"],
#     "paint": ["mspaint.exe"],
#     "chrome": find_chrome()
# }

# def main():

#     print("Welcome to Application Runner! yolo")

#     input_choice = input("Please Choose if you like to input using a keyboard or the Microphone. \n 1.Keyboard \n 2.Microphone")
#     while True:
#         if (input_choice == "1"):
#             print("Available applications1:")
#             print("1. Notepad")
#             print("2. Calculator")
#             print("3. Paint")
#             print("4. Chrome")
#             app = input("Enter the name or question of the application you want to run: ")
#             app = app.lower()
#             if "notepad" in app:
#                 subprocess.Popen(app_map["notepad"])
#             elif "calculator" in app or "calc" in app:
#                 subprocess.Popen(app_map["calculator"])
#             elif "paint" in app:
#                 subprocess.Popen(app_map["paint"])
#             elif "chrome" in app or "browser" in app:
#                 if app_map["chrome"]:
#                     subprocess.Popen(app_map["chrome"])
#                 else:
#                     print("Google Chrome not found.")
#             else:
#                 print("Application not found. Please try again.")
#         elif (input_choice == "2"):
#             print("Available applications2:")
#             print("1. Notepad")
#             print("2. Calculator")
#             print("3. Paint")
#             print("4. Chrome")
#             app = voice_recognizing()
#             app = app.lower()
#             if "notepad" in app:
#                 subprocess.Popen(app_map["notepad"])
#             elif "calculator" in app or "calc" in app:
#                 subprocess.Popen(app_map["calculator"])
#             elif "paint" in app:
#                 subprocess.Popen(app_map["paint"])
#             elif "chrome" in app or "browser" in app:
#                 if app_map["chrome"]:
#                     subprocess.Popen(app_map["chrome"])
#                 else:
#                     print("Google Chrome not found.")
#             else:
#                 print("Application not found. Please try again.")







# main()

# # while True:

# #     if "notepad" in app:
# #         subprocess.Popen(app_map["notepad"])
# #         main
# #     elif "calculator" in app or "calc" in app:
# #         subprocess.Popen(app_map["calculator"])
# #         main()
# #     elif "paint" in app:
# #         subprocess.Popen(app_map["paint"])
# #     elif "chrome" in app or "browser" in app:
# #         if app_map["chrome"]:
# #             subprocess.Popen(app_map["chrome"])
# #             main()
# #         else:
# #             print("Google Chrome not found.")
# #     elif "escape" in app:
# #         exit
# #     else:
# #         print("Application not found. Please try again.")

import speech_recognition
import subprocess
import winreg
import os

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

def find_chrome():
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.OpenKey(reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe")
        path = winreg.QueryValue(key, None)
        winreg.CloseKey(key)
        return path
    except WindowsError:
        return None

app_map = {
    "notepad": ["notepad.exe"],
    "calculator": ["calc.exe"],
    "paint": ["mspaint.exe"],
    "chrome": find_chrome()
}

def main():
    print("Welcome to Application Runner!\n")
    input_choice = input("Please Choose if you like to input using a keyboard or the Microphone.\n1. Keyboard\n2. Microphone\n")

    while True:
        if input_choice == "1":
            print("Available applications:")
            print("1. Notepad")
            print("2. Calculator")
            print("3. Paint")
            print("4. Chrome")
            print("5. Exit")
            app_input = input("Enter the name or question of the application you want to run: ").lower()
        elif input_choice == "2":
            print("Available applications:")
            print("1. Notepad")
            print("2. Calculator")
            print("3. Paint")
            print("4. Chrome")
            print("5. Exit")
            app_input = voice_recognizing()

        if "notepad" in app_input:
            subprocess.Popen(app_map["notepad"])
        elif "calculator" in app_input or "calc" in app_input:
            subprocess.Popen(app_map["calculator"])
        elif "paint" in app_input:
            subprocess.Popen(app_map["paint"])
        elif "chrome" in app_input or "browser" in app_input:
            if app_map["chrome"]:
                subprocess.Popen(app_map["chrome"])
            else:
                print("Google Chrome not found.")
        # elif "exit" in app_input:
        #     os._exit(0)
        else:
            print("Application not found. Please try again.")

main()

