@echo off
SETLOCAL

:: Check for Python installation and version
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed or not found in the system PATH.
    echo Please install Python 3.11.9 from https://www.python.org/ and rerun this script.
    GOTO :EOF
)

echo Python is installed.
echo Checking for virtual environment...
IF NOT EXIST ".venv\" (
    echo Creating virtual environment...
    python -m venv .venv
    echo Virtual environment created.
) ELSE (
    echo Virtual environment already exists.
)

echo Activating virtual environment...
CALL .venv\Scripts\activate.bat

echo Installing required packages from requirements.txt...
pip install -r requirements.txt

echo Setup complete.
ENDLOCAL