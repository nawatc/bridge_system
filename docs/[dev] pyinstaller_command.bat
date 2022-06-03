@echo off

pyinstaller -F --add-data "dds-64.dll;." --icon="icon.ico" --noconsole main_windows.py

rem -F --add-data "dds-64.dll;." --icon="icon.ico" --noconsole main_windows.py
rem add icon.ico file in diractory

pause
