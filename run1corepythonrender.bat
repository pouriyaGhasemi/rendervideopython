@echo off
setlocal enableextensions disabledelayedexpansion

set /p Build=<mustrun.txt

set "now=%time: =0%"

set "task=day"
if "%now%" gtr "03:00:00,00" (if "%now%" lss "10:15:00,00" (start "C:\Program Files (x86)\Python37-32\python.exe" python "E:\limoonad render logo\c4\views.py" ) else ( if "%now%" lss "11:20:00,00" (start  "C:\Program Files (x86)\Python37-32\python.exe" python "E:\limoonad render logo\c4\views.py" ) else ( if "%now%" lss "22:35:00,00" (if "%now%" gtr "20:00:18,00" (start  "C:\Program Files (x86)\Python37-32\python.exe" python "E:\limoonad render logo\c4\views.py")   ))))
if "%now%" lss "23:59:00,00" if "%now%" gtr "23:45:18,00" (start  "C:\Program Files (x86)\Python37-32\python.exe" python "E:\limoonad render logo\c4\tryagain.py")