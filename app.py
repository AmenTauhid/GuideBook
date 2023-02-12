import subprocess
import winreg
import platform
import os
import tkinter as tk
from tkinter import messagebox

# paint_button = tk.Button(root, text="Paint", command=lambda: run_app("paint"))
# paint_button.pack()

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
    elif app_map[app_name]:
        subprocess.Popen(app_map[app_name])
    else:
        messagebox.showerror("Error", f"{app_name.capitalize()} not found.")

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
root.mainloop()