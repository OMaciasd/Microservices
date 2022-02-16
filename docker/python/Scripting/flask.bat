@echo off

rem Variables...
set RUTA=C:\Python311\Scripts

rem Deleting...
rmdir /S /Q C:\Python311\Lib\site-packages

rem Piping...
Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
python get-pip.py

rem Installing...
pip install Flask

rem Setting...
echo Agregando %RUTA% al PATH...
setx PATH "%PATH%;%RUTA%"
echo Listo.

echo Proceso finalizado.
pause
