@echo off
cls

rem Setting Variable
set foldername=build_program

rem Create build folder
cd ..
mkdir %foldername%

rem Run Pyinstaller
pyinstaller -F --add-data "dds-64.dll;." --icon="icon.ico" --noconsole gui_interface.py

rem Copy to build folder
xcopy /Q	%cd%\dist\gui_interface.exe 	%cd%\%foldername%
xcopy /Q	%cd%\icon.ico 			%cd%\%foldername%
xcopy /Q	%cd%\dds-64.dll		 	%cd%\%foldername%
mkdir %cd%\%foldername%\picture_resource
xcopy /S	%cd%\picture_resource		%cd%\%foldername%\picture_resource
xcopy /Q	%cd%\bridge_board_sample.db	%cd%\%foldername%
xcopy /Q	%cd%\org_seed			%cd%\%foldername%
xcopy /Q	%cd%\seed			%cd%\%foldername%

rem Clean build folder
del /Q 		%cd%\gui_interface.spec
rmdir /S /Q 	%cd%\build
rmdir /S /Q 	%cd%\dist

rem Rename Folder to build
rename %cd%\build_program	build

rem Return to start folder
cls
cd docs
echo build folder had been made. !

