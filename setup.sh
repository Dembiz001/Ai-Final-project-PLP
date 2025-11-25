#!/bin/bash

# AI Garden Assistant - Quick Start Script
# This script sets up and runs both frontend and backend

echo "🌱 AI Garden Assistant - Quick Start"
echo "====================================="
echo ""

# Check for required tools
command -v python3 &> /dev/null || { echo "❌ Python 3 is required"; exit 1; }
command -v node &> /dev/null || { echo "❌ Node.js is required"; exit 1; }
command -v npm &> /dev/null || { echo "❌ npm is required"; exit 1; }

echo "✅ All prerequisites installed"
echo ""

# Backend setup
echo "📦 Setting up Backend..."
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux; use venv\Scripts\activate for Windows

# Install dependencies
pip install -r requirements.txt

# Create uploads directory
mkdir -p uploads

echo "✅ Backend ready at http://localhost:5000"
echo ""

# Frontend setup
echo "📦 Setting up Frontend..."
cd ../frontend

# Install dependencies
npm install

echo "✅ Frontend ready at http://localhost:3000"
echo ""

echo "🚀 Ready to start!"
echo ""
echo "To start the application:"
echo "1. In one terminal: cd backend && source venv/bin/activate && python app.py"
echo "2. In another terminal: cd frontend && npm start"
