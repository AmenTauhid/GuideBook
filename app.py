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

# def find_exe(exe_name):
#     if platform.system() == "Windows":
#         try:
#             reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
#             key = winreg.OpenKey(reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe")
#             path = winreg.QueryValue(key, None)
#             winreg.CloseKey(key)
#             return path
#         except WindowsError:
#             return None
#     elif platform.system() == "Darwin":
#         try:
#             path = subprocess.check_output(["mdfind", exe_name]).strip().decode("utf-8")
#         except subprocess.CalledProcessError:
#             return None
#     else:
#         return None
#     return path

print("Welcome to Application Runner!")
print("Available applications:")
print("1. Notepad")
print("2. Calculator")
print("3. Paint")
print("4. Chrome")

app = int(input("Enter the number of the application you want to run: "))

if app == 1:
    subprocess.Popen(["notepad.exe"])
elif app == 2:
    subprocess.Popen(["calc.exe"])
elif app == 3:
    import subprocess
    subprocess.Popen(["mspaint.exe"])
elif app == 4:
    chrome_path = find_chrome()
    if chrome_path:
        subprocess.Popen([chrome_path])
    else:
        print("Google Chrome not found.")
    # chrome_path = find_exe("Google Chrome.app")
    # if chrome_path is not None:
    #     subprocess.Popen(["open", "-a", chrome_path])
    # else:
    #     print("Google Chrome could not be found.")
else:
    print("Invalid option. Please enter a number between 1 and 3.")
    
    
