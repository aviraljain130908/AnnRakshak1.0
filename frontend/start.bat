@echo off
setlocal

echo ===============================================
echo   AnnRakshak Frontend - starting local server
echo ===============================================
echo.
echo Once started, open this in your browser:
echo     http://localhost:3000
echo.
echo IMPORTANT: Do NOT open index.html by double-clicking it.
echo Opening it directly (file://) will always show
echo "Backend unreachable" because of browser security (CORS).
echo Always use the http://localhost:3000 link above instead.
echo.

where python >nul 2>nul
if %errorlevel%==0 (
    echo Starting server with Python...
    echo.
    python -m http.server 3000
    goto :end
)

where py >nul 2>nul
if %errorlevel%==0 (
    echo Starting server with Python launcher...
    echo.
    py -m http.server 3000
    goto :end
)

where npx >nul 2>nul
if %errorlevel%==0 (
    echo Python not found - trying Node.js instead...
    echo.
    npx --yes serve -l 3000 .
    goto :end
)

echo ERROR: Could not find Python or Node.js on this system.
echo.
echo Please install one of the following and try again:
echo   - Python:  https://www.python.org/downloads/
echo   - Node.js: https://nodejs.org/
echo.

:end
echo.
echo Server stopped ^(or failed to start - see any errors above^).
pause
