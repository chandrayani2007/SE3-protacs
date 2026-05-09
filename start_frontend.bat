@echo off
echo ===================================================
echo     Starting SE3-PROTACs Web Server
echo ===================================================
echo.
echo Starting the FastAPI backend in a new window...

:: Start the server in a new command prompt window
:: We use 'call conda activate' to ensure the environment is properly loaded
start "SE3-PROTACs Server" cmd /k "call conda activate se3protacs && uvicorn app:app --host 0.0.0.0 --port 8000"

:: Wait a few seconds to let the model load and the server start
echo Waiting for the model to load and server to initialize (this may take a few seconds)...
timeout /t 7 /nobreak > nul

:: Automatically open the default web browser to the frontend
echo.
echo Opening the frontend in your default browser...
start http://localhost:8000/

echo.
echo Done! If the browser didn't open, manually go to: http://localhost:8000/
echo To stop the server later, just close the new command prompt window that opened.
echo.
pause
