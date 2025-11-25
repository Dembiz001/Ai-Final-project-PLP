@echo off
REM AI Garden Assistant - Quick Start Script (Windows)
REM This script sets up and runs both frontend and backend

echo 🌱 AI Garden Assistant - Quick Start
echo =====================================
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required. Please install Python 3.8+
    pause
    exit /b 1
)

REM Check for Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is required. Please install Node.js 14+
    pause
    exit /b 1
)

echo ✅ All prerequisites installed
echo.

REM Backend setup
echo 📦 Setting up Backend...
cd backend

REM Create virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Create uploads directory
if not exist uploads mkdir uploads

echo ✅ Backend ready at http://localhost:5000
echo.

REM Frontend setup
echo 📦 Setting up Frontend...
cd ..\frontend

REM Install dependencies
call npm install

echo ✅ Frontend ready at http://localhost:3000
echo.

echo 🚀 Ready to start!
echo.
echo To start the application:
echo 1. In one terminal: cd backend ^& venv\Scripts\activate ^& python app.py
echo 2. In another terminal: cd frontend ^& npm start
echo.
pause
