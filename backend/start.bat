@echo off
REM Run this from inside the Sih-backend folder.

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

echo Installing dependencies (first run only takes a while)...
pip install -r requirements.txt

echo Starting backend at http://127.0.0.1:8000 ...
python run.py
