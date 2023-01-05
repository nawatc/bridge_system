rem Remove build DIR
cd ..
rmdir /S /Q 	%cd%\build 
del /Q 		%cd%\docs\bridge_system.exe

rem Return to start folder
cls
cd docs
echo clean !
