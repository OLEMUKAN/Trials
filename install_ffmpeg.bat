@echo off
echo FFmpeg Installation for YouTube Downloader
echo ==========================================
echo.

REM Check if FFmpeg is already installed
ffmpeg -version >nul 2>&1
if %errorlevel% == 0 (
    echo ✅ FFmpeg is already installed and accessible!
    ffmpeg -version | findstr "ffmpeg version"
    echo.
    pause
    exit /b 0
)

echo FFmpeg is not installed or not in PATH.
echo.
echo This YouTube downloader needs FFmpeg for:
echo - Converting audio formats (MP3 extraction)
echo - Merging video and audio streams
echo - Processing various video formats
echo.
echo Please choose an installation method:
echo.
echo 1. Download FFmpeg manually (Recommended)
echo 2. Install via Chocolatey (if you have it)
echo 3. Install via Winget (Windows 10/11)
echo 4. Exit and install later
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto manual
if "%choice%"=="2" goto chocolatey
if "%choice%"=="3" goto winget
if "%choice%"=="4" goto exit

echo Invalid choice. Please run the script again.
pause
exit /b 1

:manual
echo.
echo Manual Installation Instructions:
echo ================================
echo.
echo 1. Go to: https://www.gyan.dev/ffmpeg/builds/
echo 2. Download "release builds" - "ffmpeg-release-essentials.zip"
echo 3. Extract to C:\ffmpeg (create this folder)
echo 4. Add C:\ffmpeg\bin to your system PATH
echo.
echo Detailed steps:
echo - Right-click "This PC" → Properties → Advanced System Settings
echo - Click "Environment Variables"
echo - Under System Variables, find "Path" and click Edit
echo - Click "New" and add: C:\ffmpeg\bin
echo - Click OK on all windows
echo - Restart your terminal/command prompt
echo.
echo Opening download page in your browser...
start https://www.gyan.dev/ffmpeg/builds/
pause
goto exit

:chocolatey
echo.
echo Installing FFmpeg via Chocolatey...
choco install ffmpeg -y
if %errorlevel% == 0 (
    echo ✅ FFmpeg installed successfully via Chocolatey!
) else (
    echo ❌ Chocolatey installation failed. Try manual installation.
)
pause
goto exit

:winget
echo.
echo Installing FFmpeg via Winget...
winget install --id=Gyan.FFmpeg -e
if %errorlevel% == 0 (
    echo ✅ FFmpeg installed successfully via Winget!
) else (
    echo ❌ Winget installation failed. Try manual installation.
)
pause
goto exit

:exit
echo.
echo After installing FFmpeg, restart your terminal and run the YouTube downloader again.
echo You can test FFmpeg installation by running: ffmpeg -version
echo.
pause
