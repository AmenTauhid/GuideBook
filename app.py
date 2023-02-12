import subprocess
import winreg
import platform
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

testUiClass.mainStart()

    