import tkinter as tk
from tkinter import messagebox
from app import mainApp
from VoiceRecognition.voiceRecog import voiceRecogClass

class testUiClass:

    def tinkerUifunc():
        root = tk.Tk()
        root.geometry("200x200")
        root.title("Application Runner")

        notepad_button = tk.Button(root, text="Notepad", command=lambda: mainApp.run_app("notepad"))
        notepad_button.pack()

        calculator_button = tk.Button(root, text="Calculator", command=lambda:mainApp.run_app("calculator"))
        calculator_button.pack()

        paint_button = tk.Button(root, text="Paint", command=lambda: mainApp.run_app("paint"))
        paint_button.pack()

        chrome_button = tk.Button(root, text="Chrome", command=lambda: mainApp.run_app("chrome"))
        chrome_button.pack()

        photo_button = tk.Button(root, text="Photos", command=lambda: mainApp.run_app("photos"))
        photo_button.pack()

        clock_button = tk.Button(root, text="Weather", command=lambda: mainApp.run_app("weather"))
        clock_button.pack()

        calendar_button = tk.Button(root, text="Calendar", command=lambda: mainApp.run_app("calendar"))
        calendar_button.pack()

        camera_button = tk.Button(root, text="Camera", command=lambda: mainApp.run_app("camera"))
        camera_button.pack()

        root.mainloop()

    def mainStart():
        print("Welcome to Application Runner!\n")
        input_choice = input("Please Choose if you like to input using a keyboard/mouse or the Microphone.\n1. Keyboard\n2. Microphone\n")

        while True:
            if input_choice == "1":
                print("Available applications:")
                print("1. Notepad")
                print("2. Calculator")
                print("3. Paint")
                print("4. Chrome")
                print("5. Exit")
                # app_input = input("Enter the name or question of the application you want to run: ").lower()
                testUi.tinkerUiFunc()
                break
            elif input_choice == "2":
                print("Available applications:")
                print("1. Notepad")
                print("2. Calculator")
                print("3. Paint")
                print("4. Chrome")
                print("5. Exit")
                app_input = voiceRecogClass.voice_recognizing()
                voiceRecogClass.find_app_from_voice(app_input)
        
