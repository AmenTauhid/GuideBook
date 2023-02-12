import subprocess
import winreg
import platform
import speech_recognition
import os
import tkinter as tk
from tkinter import messagebox
from UI.testUi import testUiClass

class mainApp:

    def find_app(app_name):
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            key = winreg.OpenKey(reg, f"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\{app_name}.exe")
            path = winreg.QueryValue(key, None)
            winreg.CloseKey(key)
            return path
        except WindowsError:
            return None

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

    def run_app(app_name):
        if app_name=="weather":
            os.system('start explorer shell:appsfolder\Microsoft.BingWeather_8wekyb3d8bbwe!App')
        elif app_name=="photos":
            os.system('start explorer shell:appsfolder\Microsoft.Windows.Photos_8wekyb3d8bbwe!App')
        elif app_name=="calendar":
            os.system('start explorer shell:appsfolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar')
        elif app_name=="camera":
            os.system('start explorer shell:appsfolder\Microsoft.WindowsCamera_8wekyb3d8bbwe!App')    
        elif mainApp.app_map[app_name]:
            subprocess.Popen(mainApp.app_map[app_name])
        else:
            messagebox.showerror("Error", f"{app_name.capitalize()} not found.")


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

root = tk.Tk()
root.geometry("200x200")
root.title("Application Runner")

notepad_button = tk.Button(root, text="Notepad", command=lambda: run_app("notepad"))
notepad_button.pack()

calculator_button = tk.Button(root, text="Calculator", command=lambda: run_app("calculator"))
calculator_button.pack()

paint_button = tk.Button(root, text="Paint", command=lambda: run_app("paint"))
paint_button.pack()

chrome_button = tk.Button(root, text="Chrome", command=lambda: run_app("chrome"))
chrome_button.pack()

photo_button = tk.Button(root, text="Photos", command=lambda: run_app("photos"))
photo_button.pack()

clock_button = tk.Button(root, text="Weather", command=lambda: run_app("weather"))
clock_button.pack()

calendar_button = tk.Button(root, text="Calendar", command=lambda: run_app("calendar"))
calendar_button.pack()

camera_button = tk.Button(root, text="Camera", command=lambda: run_app("camera"))
camera_button.pack()

def find_app_by_voice(app_input):
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
            root.mainloop()
        elif input_choice == "2":
            print("Available applications:")
            print("1. Notepad")
            print("2. Calculator")
            print("3. Paint")
            print("4. Chrome")
            print("5. Exit")
            app_input = voice_recognizing()
            find_app_by_voice(app_input)
main()