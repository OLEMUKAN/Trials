# YouTube Video Downloader

A modern, user-friendly YouTube video downloader with a graphical interface built using Python and tkinter.

## Features

- **Modern Dark Theme GUI** - Clean and intuitive interface
- **Multiple Format Support** - Download videos in MP4, MP3, WebM, MKV, AVI formats
- **Quality Selection** - Choose from various quality options (720p, 480p, 360p, etc.)
- **Video Information** - Get detailed video information before downloading
- **Progress Tracking** - Real-time download progress with speed information
- **Custom Download Path** - Choose where to save your downloads
- **Detailed Logging** - View download progress and any issues in the log area

## Requirements

- Python 3.7 or higher
- Windows, macOS, or Linux
- Internet connection

## Installation

1. **Clone or download this repository**

2. **Install Python requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg (Required):**
   
   FFmpeg is essential for audio extraction and video processing.
   
   **Windows:**
   - **Easy way**: Run `install_ffmpeg.bat` (included in this package)
   - **Manual way**: 
     - Download from [FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/)
     - Extract to `C:\ffmpeg`
     - Add `C:\ffmpeg\bin` to your system PATH
   
   **macOS:**
   ```bash
   brew install ffmpeg
   ```
   
   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
   
   **Verify installation:**
   ```bash
   ffmpeg -version
   ```

4. **Run the application:**
   ```bash
   python youtube_downloader.py
   ```

## Usage

1. **Enter YouTube URL** - Paste the YouTube video URL in the URL field
2. **Select Format** - Choose your preferred video/audio format
3. **Select Quality** - Choose the quality (best, worst, or specific resolution)
4. **Choose Download Path** - Select where to save the file (default: Downloads folder)
5. **Get Video Info** (Optional) - Click to view video details before downloading
6. **Download** - Click "Download Video" to start the download

## Supported URLs

- Standard YouTube URLs: `https://www.youtube.com/watch?v=...`
- Short URLs: `https://youtu.be/...`
- Playlist URLs (downloads individual videos)

## Features in Detail

### Format Options
- **MP4** - Standard video format (most compatible)
- **MP3** - Audio-only downloads
- **WebM** - Google's open video format
- **MKV** - Matroska video format
- **AVI** - Legacy video format

### Quality Options
- **Best** - Highest available quality
- **Worst** - Lowest available quality
- **720p, 480p, 360p, 240p, 144p** - Specific resolutions

### Video Information
The "Get Video Info" button provides:
- Video title and description
- Duration and upload date
- View count and uploader information
- Available formats and file sizes

## Technical Details

This application uses:
- **yt-dlp** - Powerful YouTube downloading library (fork of youtube-dl)
- **tkinter** - GUI framework (included with Python)
- **Threading** - For non-blocking downloads and UI responsiveness

## Troubleshooting

### Common Issues

1. **"No module named 'yt_dlp'"**
   - Install with: `pip install yt-dlp`

2. **"FFmpeg not found" or audio conversion errors**
   - **Windows**: Run `install_ffmpeg.bat` or download from [FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/)
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`
   - Verify with: `ffmpeg -version`

3. **Download fails with "Video unavailable"**
   - Video might be private, deleted, or region-restricted
   - Try updating yt-dlp: `pip install --upgrade yt-dlp`

4. **Slow download speeds**
   - This depends on your internet connection and YouTube's servers
   - Try downloading at different times

5. **Audio-only downloads not working**
   - This is usually due to missing FFmpeg (see issue #2 above)
   - FFmpeg is required for MP3 conversion and audio extraction

6. **Format selection issues (downloading wrong quality)**
   - Always use "Load Video & Get Qualities" first
   - Select the exact quality from the dropdown (shows format IDs)
   - Avoid generic "best" option for precise quality control

### Error Messages

- Check the log area for detailed error information
- Most issues are related to network connectivity or video availability

## Legal Notice

This tool is for educational purposes and personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download videos you have permission to download or that are in the public domain.

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this application.

## Changelog

### Version 1.0
- Initial release with basic download functionality
- Dark theme GUI
- Multiple format and quality options
- Video information retrieval
- Progress tracking and logging
