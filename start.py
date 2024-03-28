from tkinter import *
import time
import socket
from os import system
print("Welcome to Endermanch Downloader v1.0.0!\nTesting connection...")


def check_internet():
  try:
    socket.create_connection(("www.google.com", 80))
    return True
  except OSError:
    pass
  return False

if check_internet():
  print("Active internet connection, proceeding with download...")
else: 
  print("No active internet connection, please make sure you are connected to the Internet and try again")
  system("timeout -1")
  system("start.py")
  exit()
system("PowerShell -Command Invoke-WebRequest -Uri http://mdl2.x10.mx/wget.exe -OutFile .\wget.exe")
print("Downloading latest files...")
system("wget.exe http://mdl2.x10.mx/gsudo.exe")
print("Download complete!")
q1 = input("View software-listing.txt? (Y/N): ")
if q1 == "y" or "Y":
  system("wget https://dl.malwarewatch.org/software-listing.txt")
#  Disabled because it was triggering even without a Y input
#  system("notepad software-listing.txt")
  system("del software-listing.txt")
else:
    print("No file viewing selected, continuing...")
def download_file(path):
  system(f"wget.exe http://dl.malwarewatch.org/{path}")
print("Available downloads:")
print("1. WinToUSB\n2. WGet\n3. EaseUS Partition Master\n4. Virtual PC 2007 x32\n5. Virtual Pc 2007 x64\n6. Uninstall Tool\n7. UltraISO\n8.Exit")
askdownload = input("What would you like to download? Select with a number:")
if askdownload == "1":
  download_file("software/useful/WinToUSB.7z")

elif askdownload == "2":
    download_file("software/useful/WGet.7z")
elif askdownload == "3":
  download_file("software/useful/EaseUSPartitionMasterPE.iso")
elif askdownload == "4":
  download_file("software/useful/VirtualPC2007.7z")
elif askdownload == "5":
  download_file("software/useful/VirtualPC2007-x64.7z")
elif askdownload == "6":
  download_file("software/useful/UninstallTool.7z")
elif askdownload == "7":
  download_file("software/useful/UltraISO.7z")
else:
    print("Invalid selection, exiting...")
    system("del gsudo.exe.* wget.exe.*")
    exit()
repeat = input("Would you like to download more files? (Y/N): ")
if repeat == "y" or "Y":
  system("start.py")
  exit()
else:
  print("Exiting...")
system("del gsudo.exe.* wget.exe.*")
exit()