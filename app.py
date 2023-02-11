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

print("Welcome to Application Runner!")

question = input("Ask me to open an application: ")

if "notepad" in question:
    subprocess.Popen(["notepad.exe"])
elif "calculator" in question:
    subprocess.Popen(["calc.exe"])
elif "paint" in question:
    subprocess.Popen(["mspaint.exe"])
elif "chrome" in question:
    chrome_path = find_chrome()
    if chrome_path:
        subprocess.Popen([chrome_path])
    else:
        print("Google Chrome not found.")
else:
    print("I am sorry, I could not find the application you requested.")
