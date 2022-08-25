@echo off

pyinstaller -F --add-data "dds-64.dll;." --icon="icon.ico" --noconsole gui_interface.py

rem -F --add-data "dds-64.dll;." --icon="icon.ico" --noconsole main_windows.py
rem add icon.ico ,dds-64.dll file in diractory

pause
