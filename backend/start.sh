#!/usr/bin/env bash
# Run this from inside the Sih-backend folder.
set -e

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "Installing dependencies (first run only takes a while)..."
pip install -r requirements.txt

echo "Starting backend at http://127.0.0.1:8000 ..."
python run.py
