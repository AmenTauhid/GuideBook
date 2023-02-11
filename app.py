import subprocess

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
    subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe"])    
else:
    print("Invalid option. Please enter a number between 1 and 3.")
