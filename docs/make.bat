@echo off
cls

rem Setting Variable
set foldername=build_program

rem Create build folder
cd ..
mkdir %foldername%

rem Run Pyinstaller
rem pyinstaller -F --add-data "dds-64.dll;." --icon="icon.ico" --noconsole bridge-system-gui.py
rem pyinstaller -F --add-data "dds-64.dll;." --icon="icon.ico" --noconsole --uac-admin bridge-system-gui.py
pyinstaller -F --add-data "dds-64.dll;." --icon="icon.ico" --noconsole bridge-system-gui.py

rem Copy to build folder
xcopy /Q	%cd%\dist\bridge-system-gui.exe 	%cd%\%foldername%
xcopy /Q	%cd%\icon.ico 			%cd%\%foldername%
xcopy /Q	%cd%\dds-64.dll		 	%cd%\%foldername%
mkdir %cd%\%foldername%\picture_resource
xcopy /S	%cd%\picture_resource		%cd%\%foldername%\picture_resource
xcopy /Q	%cd%\bridge_board_sample.db	%cd%\%foldername%
xcopy /Q	%cd%\org_seed			%cd%\%foldername%
xcopy /Q	%cd%\seed			%cd%\%foldername%

rem Clean build folder
del /Q 		%cd%\bridge-system-gui.spec
rmdir /S /Q 	%cd%\build
rmdir /S /Q 	%cd%\dist

rem Rename Folder to build
rename %cd%\%foldername%\bridge-system-gui.exe	bridge_system.exe
rename %cd%\%foldername%			build

rem Return to start folder
rem cls
cd docs
echo build folder had been made. !

pause

