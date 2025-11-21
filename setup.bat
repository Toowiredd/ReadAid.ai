@echo off
REM ReadAid.ai Setup Script for Windows
REM This script helps you set up ReadAid.ai quickly and easily

echo ================================================
echo    Welcome to ReadAid.ai Setup!
echo ================================================
echo.

REM Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo [SUCCESS] Python %PYTHON_VERSION% found
echo.

REM Check pip installation
echo Checking pip installation...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not installed
    echo Please install pip
    pause
    exit /b 1
)
echo [SUCCESS] pip found
echo.

REM Create virtual environment
echo Setting up virtual environment...
if not exist "venv" (
    python -m venv venv
    echo [SUCCESS] Virtual environment created
) else (
    echo [WARNING] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo [SUCCESS] Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo [SUCCESS] pip upgraded
echo.

REM Install dependencies
echo Installing dependencies...
echo (This may take a few minutes...)
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [SUCCESS] Dependencies installed
echo.

REM Set up environment file
echo Setting up environment file...
if not exist ".env" (
    copy .env.example .env >nul
    echo [SUCCESS] .env file created from .env.example
    echo [WARNING] Please edit .env and add your API keys:
    echo   - OPENAI_API_KEY
    echo   - TAVILY_API_KEY
) else (
    echo [WARNING] .env file already exists
)
echo.

REM Check for API keys
echo Checking API keys...
findstr /C:"your_openai_api_key_here" .env >nul 2>&1
if not errorlevel 1 (
    echo [WARNING] OpenAI API key not set in .env file
    echo   Get your key at: https://platform.openai.com/api-keys
)

findstr /C:"your_tavily_api_key_here" .env >nul 2>&1
if not errorlevel 1 (
    echo [WARNING] Tavily API key not set in .env file
    echo   Get your key at: https://tavily.com/
)
echo.

REM Summary
echo ================================================
echo    Setup Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Edit .env file and add your API keys
echo 2. Run: venv\Scripts\activate.bat
echo 3. Run: streamlit run app.py
echo.
echo [SUCCESS] Happy accessible reading! 📚✨
echo.
pause
