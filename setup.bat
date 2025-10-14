@echo off
echo === Supply Chain Management DBMS Setup ===
echo.

REM Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

python --version
echo [OK] Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist venv (
    echo Virtual environment already exists.
) else (
    python -m venv venv
    echo [OK] Virtual environment created
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install requirements
echo Installing required packages...
echo This may take a few minutes...
echo NOTE: Using python-oracledb (no Oracle Instant Client needed)
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install packages
    pause
    exit /b 1
)
echo [OK] Packages installed
echo.

REM Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file...
    copy .env.example .env >nul
    echo [OK] .env file created
    echo.
    echo IMPORTANT: Edit .env file and set your Oracle database credentials:
    echo   - DB_USER
    echo   - DB_PASSWORD
    echo   - DB_DSN
) else (
    echo .env file already exists.
)
echo.

echo === Setup Complete ===
echo.
echo Next steps:
echo 1. Update .env file with your Oracle database credentials
echo 2. Run schema.sql in your Oracle database to create tables
echo 3. Run sample_data.sql to load sample data (optional)
echo 4. Start the application: run.bat
echo.
echo The application will be available at: http://localhost:5000
echo.

pause
