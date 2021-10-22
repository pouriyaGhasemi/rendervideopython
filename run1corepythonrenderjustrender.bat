@echo off
setlocal enableextensions disabledelayedexpansion

set /p Build=<mustrun.txt

set "now=%time: =0%"

set "task=day"
if "%now%" gtr "01:05:00,00" (if "%now%" lss "01:00:00,00" (start /affinity 15 "C:\Program Files (x86)\Python37-32\python.exe" python "E:\limoonad render logo\c4\justrender.py" ) else ( if "%now%" lss "09:40:00,00" (start /affinity 31 "C:\Program Files (x86)\Python37-32\python.exe" python "E:\limoonad render logo\c4\justrender.py" ) else ( if "%now%" lss "9:00:00,00" if "%now%" gtr "10:45:00,00" (start /affinity 1 "C:\Program Files (x86)\Python37-32\python.exe" python "E:\limoonad render logo\c4\justrender.py" ))))