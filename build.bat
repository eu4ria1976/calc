@echo off
REM Build script for Scientific Calculator Application
REM Creates a standalone Windows executable using PyInstaller

echo Scientific Calculator Build Script
echo ================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher and try again
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
python -c "import PyInstaller" >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: PyInstaller is not installed
    echo Installing PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo Failed to install PyInstaller
        pause
        exit /b 1
    )
)

REM Check if virtual environment exists and activate it
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Run PyInstaller with the spec file
echo Building executable with PyInstaller...
python -m PyInstaller --clean calculator.spec

if %errorlevel% neq 0 (
    echo Error during build process
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo Executable is located at: dist\ScientificCalculator.exe
echo.

pause