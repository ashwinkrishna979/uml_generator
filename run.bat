@echo off

rem Activate the virtual environment
call umlcon_env\Scripts\activate

rem Check if the virtual environment activation was successful
if %errorlevel% equ 0 (
    echo Virtual environment activated successfully
) else (
    echo Failed to activate the virtual environment
    exit /b 1
)

rem Change directory to the Django project directory
cd uml_converter

rem Start the Django server
python manage.py runserver

rem Deactivate the virtual environment after use
deactivate
