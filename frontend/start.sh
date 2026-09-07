#!/usr/bin/env bash
# Serves index.html at http://localhost:3000 (matches the backend's allowed CORS origin).
# IMPORTANT: Do NOT open index.html directly via file:// - the backend's CORS
# will block it and the page will show "Backend unreachable". Always use
# http://localhost:3000 once this script is running.

echo "==============================================="
echo "  AnnRakshak Frontend - starting local server"
echo "==============================================="
echo
echo "Once started, open this in your browser:"
echo "    http://localhost:3000"
echo

if command -v python3 >/dev/null 2>&1; then
    echo "Starting server with Python..."
    python3 -m http.server 3000
elif command -v python >/dev/null 2>&1; then
    echo "Starting server with Python..."
    python -m http.server 3000
elif command -v npx >/dev/null 2>&1; then
    echo "Python not found - trying Node.js instead..."
    npx --yes serve -l 3000 .
else
    echo "ERROR: Could not find Python or Node.js on this system."
    echo "Please install one of the following and try again:"
    echo "  - Python:  https://www.python.org/downloads/"
    echo "  - Node.js: https://nodejs.org/"
    exit 1
fi
