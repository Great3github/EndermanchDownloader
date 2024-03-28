from os import system
import socket
system("cls")
print("Updating, please wait...")
system("del start.py start.py.* gsudo.exe gsudo.exe.* wget.exe wget.exe.*")
def check_internet():
  try:
    socket.create_connection(("mdl2.x10.mx", 80))
    return True
  except OSError:
    pass
  return False

if check_internet():
  print("Active internet connection, proceeding with download...")
else: 
  print("No active internet connection or server is down, please make sure you are connected to the Internet and try again later")
  exit()
system("PowerShell -Command Invoke-WebRequest -Uri http://mdl2.x10.mx/wget.exe -OutFile .\wget.exe")
system("wget http://mdl2.x10.mx/start.py")
print("Update complete, restart?")
restart = input("(Y/N): ")
if restart == "y":
    system("start.py")
    exit()