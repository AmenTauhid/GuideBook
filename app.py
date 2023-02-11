import subprocess
import winreg
import platform

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

print("Welcome to Application Runner!")
print("Available applications:")
print("1. Notepad")
print("2. Calculator")
print("3. Paint")
print("4. Chrome")

while True:
    app = input("Enter the name or question of the application you want to run: ")
    app = app.lower()
    
    if "notepad" in app:
        subprocess.Popen(app_map["notepad"])
    elif "calculator" in app or "calc" in app:
        subprocess.Popen(app_map["calculator"])
    elif "paint" in app:
        subprocess.Popen(app_map["paint"])
    elif "chrome" in app or "browser" in app:
        if app_map["chrome"]:
            subprocess.Popen(app_map["chrome"])
        else:
            print("Google Chrome not found.")
    else:
        print("Application not found. Please try again.")
