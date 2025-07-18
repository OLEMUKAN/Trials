#!/usr/bin/env python3
"""
FFmpeg Checker and Installer Helper
Checks if FFmpeg is available and provides installation guidance.
"""

import subprocess
import sys
import os
import platform

def check_ffmpeg():
    """Check if FFmpeg is installed and accessible"""
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            # Extract version info
            version_line = result.stdout.split('\n')[0]
            print(f"✅ FFmpeg is installed: {version_line}")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
        pass
    
    print("❌ FFmpeg is not installed or not accessible")
    return False

def get_installation_instructions():
    """Get OS-specific installation instructions"""
    system = platform.system().lower()
    
    instructions = {
        'windows': """
Windows Installation Options:

1. 🚀 EASY WAY (Run the provided script):
   - Double-click 'install_ffmpeg.bat' in this folder
   
2. 📥 MANUAL DOWNLOAD:
   - Go to: https://www.gyan.dev/ffmpeg/builds/
   - Download 'ffmpeg-release-essentials.zip'
   - Extract to C:\\ffmpeg
   - Add C:\\ffmpeg\\bin to your system PATH
   
3. 📦 PACKAGE MANAGERS:
   - Chocolatey: choco install ffmpeg
   - Winget: winget install Gyan.FFmpeg

""",
        'darwin': """
macOS Installation:

1. 🍺 HOMEBREW (Recommended):
   brew install ffmpeg

2. 📦 MACPORTS:
   sudo port install ffmpeg

3. 📥 MANUAL DOWNLOAD:
   - Download from: https://evermeet.cx/ffmpeg/
   - Place in /usr/local/bin/

""",
        'linux': """
Linux Installation:

1. 📦 UBUNTU/DEBIAN:
   sudo apt update
   sudo apt install ffmpeg

2. 📦 FEDORA/RHEL:
   sudo dnf install ffmpeg

3. 📦 ARCH LINUX:
   sudo pacman -S ffmpeg

4. 📥 MANUAL BUILD:
   Download from: https://ffmpeg.org/download.html

"""
    }
    
    return instructions.get(system, instructions['linux'])

def main():
    """Main function to check FFmpeg and provide guidance"""
    print("🎬 FFmpeg Installation Checker")
    print("=" * 40)
    
    if check_ffmpeg():
        print("\n🎉 Great! FFmpeg is ready for the YouTube downloader.")
        print("You can now use all features including:")
        print("- Audio extraction (MP3)")
        print("- Video format conversion")
        print("- Stream merging")
        return True
    else:
        print("\n⚠️  FFmpeg is required for the YouTube downloader to work properly.")
        print("\nWithout FFmpeg, you may experience:")
        print("- Audio extraction failures")
        print("- Format conversion errors")
        print("- Stream merging issues")
        
        print(get_installation_instructions())
        
        print("After installation, restart your terminal and run this script again to verify.")
        return False

if __name__ == "__main__":
    success = main()
    
    if not success:
        input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
