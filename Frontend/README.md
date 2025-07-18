YouTube Downloader & AI Subtitle Generator Frontend
This project is a React-based frontend for a YouTube downloader and AI subtitle generator, built with Vite for fast development and hot module replacement (HMR). It provides a modern, responsive, and interactive UI that integrates with a Python backend for video downloading and subtitle generation.
Features

Video Input: Upload local video files (.mp4, .mkv, .mov, .avi, etc.) or paste YouTube URLs.
AI Model Selection: Choose from Whisper AI model sizes (tiny, base, small, medium, large) for subtitle generation.
Language Selection: Select languages (Chinese, English, Auto, Spanish, etc.) for subtitle generation.
Subtitle Format: Generate subtitles in srt, vtt, txt, or json formats.
Translation: Option to translate subtitles to English.
YouTube Download: Download videos in various qualities (up to 1080p or higher) and formats (mp4, mp3, webm, etc.).
Subtitle Download: Download YouTube subtitles (manual or auto-generated) without video.
Output Path: Specify output directory (default: ~/Downloads) or access download links.
Progress and Status: Real-time progress bar and status messages for processing tasks.
Log Display: Scrollable log area for detailed processing information.
Theme Support: Dark/light themes with a modern, responsive design using Tailwind CSS.

Tech Stack

Frontend: React, Vite, Tailwind CSS
Dependencies: Loaded via cdn.jsdelivr.net for React, React DOM, and other libraries
Backend: Python (integrates with subs.py for subtitle generation and youtube_downloader.py for YouTube downloading)
Linting: ESLint with React and Vite configurations
Optional: TypeScript support for type safety

Getting Started
Prerequisites

Node.js (v16 or higher)
npm or yarn
Python backend API (to be developed, based on subs.py and youtube_downloader.py)

Installation

Clone the repository:git clone <repository-url>
cd <repository-name>


Install dependencies:npm install


Create a .env file in the project root to configure the backend API URL:VITE_API_URL=http://localhost:5000


Start the development server:npm run dev


Open your browser at the provided local address (typically http://localhost:5173).

Building for Production

Build the project:npm run build


Serve the production build:npm run preview



Backend Integration
The frontend is designed to integrate with a Python backend API that handles:

Video processing and subtitle generation using Whisper AI (subs.py).
YouTube video and subtitle downloading using yt-dlp (youtube_downloader.py).
API endpoints to be implemented:
/upload-video: Upload local video for subtitle generation.
/download-youtube: Download YouTube video or subtitles.
/generate-subtitles: Generate subtitles for uploaded or downloaded videos.
/get-video-info: Retrieve available qualities and subtitles for a YouTube URL.



Ensure the backend API is running and accessible at the URL specified in VITE_API_URL.
Customization

UI: Modify components in src/components/ to match your branding or workflow.
Styling: Update Tailwind CSS classes in components or add custom styles in src/styles/.
API: Adjust API calls in src/api/ to match backend endpoint specifications.
TypeScript: Integrate TypeScript for type safety by following the Vite TypeScript template and adding typescript-eslint.

Project Structure
src/
├── components/          # Reusable React components
│   ├── VideoInput.js
│   ├── ModelSelector.js
│   ├── LanguageSelector.js
│   ├── SubtitleFormatSelector.js
│   ├── TranslationToggle.js
│   ├── OutputPathSelector.js
│   ├── ProgressBar.js
│   ├── LogDisplay.js
│   ├── ActionButtons.js
├── api/                # API request handlers
├── utils/              # Utility functions
├── styles/             # Custom CSS (if not using Tailwind exclusively)
├── App.jsx             # Main app component
├── main.jsx            # Entry point

ESLint Configuration
The project includes ESLint with React and Vite plugins. To expand for production:

Add TypeScript support with typescript-eslint for type-aware linting.
Update .eslintrc to include custom rules as needed.

Known Limitations

Form submissions must avoid <form> with onSubmit due to sandbox restrictions. Use button clicks and state management instead.
Backend API is not yet implemented; mock responses may be needed for development.
Large video uploads may require chunked upload handling in the backend.

License
MIT