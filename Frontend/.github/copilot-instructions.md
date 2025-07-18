GitHub Copilot Instructions for YouTube Downloader and AI Subtitle Generator Frontend

This file provides workspace-specific instructions for GitHub Copilot to guide the development of a React frontend for a YouTube downloader and AI subtitle generator. The frontend interacts with a Python backend (subs.py and youtube_downloader.py) that handles video processing and subtitle generation.

Project Overview

The project is a modern, interactive React frontend built with Vite, designed to provide a seamless user experience for downloading YouTube videos and generating AI-powered subtitles. The UI should be responsive, support dark/light themes, and integrate with a Python backend API.

Development Guidelines

General Requirements





Framework: Use React with Vite for fast development and hot module replacement (HMR).



Styling: Use Tailwind CSS for responsive, modern, and consistent styling.



CDN Dependencies: Include React and related dependencies via cdn.jsdelivr.net to ensure compatibility and ease of deployment.



JSX: Prefer JSX over React.createElement for component definitions.



Form Handling: Avoid using <form> with onSubmit due to sandboxed frame restrictions (allow-forms not set). Use button onClick handlers or state-driven submissions instead.



Attributes: Use className instead of class for JSX elements.



Components: Create reusable, modular React components for UI elements like video upload, URL input, model selection, language selection, subtitle format, translation toggle, progress bar, and log display.



State Management: Use React hooks (useState, useEffect, etc.) for state and side effects. Avoid external state management libraries unless explicitly required.



Responsive Design: Ensure the UI is responsive across devices (mobile, tablet, desktop).



Theme Support: Implement dark and light themes, defaulting to a dark theme to match the Python backend UI (#2b2b2b background, #ffffff text, #1e1e1e for logs).

Backend Integration





API Endpoints: Prepare to connect to a Python backend API (to be developed) that exposes endpoints for:





Video upload (subs.py functionality for local video processing).



YouTube video downloading (youtube_downloader.py functionality).



AI subtitle generation using Whisper (subs.py).



Retrieving video information (qualities, subtitles) from YouTube URLs.



API Communication: Use fetch or axios for HTTP requests to the backend. Ensure proper error handling and loading states.



Data Flow:





Accept user inputs for video file/YouTube URL, AI model size (tiny, base, small, medium, large), language (zh, en, auto, etc.), subtitle format (srt, vtt, txt, json), and translation toggle.



Display progress updates and logs from backend processing.



Provide download links or file paths for generated subtitles and downloaded videos.

UI Components





Video Input:





Allow users to upload a local video file (supported formats: .mp4, .mkv, .mov, .avi, etc., as defined in subs.py).



Provide an input field for pasting YouTube URLs.



Model Selection:





Dropdown for AI model sizes (tiny, base, small, medium, large) with tooltips or labels indicating speed/accuracy trade-offs (e.g., "Tiny: Fastest, least accurate (~39 MB)").



Language Selection:





Dropdown for languages (zh, en, auto, es, fr, etc.) with human-readable names (e.g., "Chinese" instead of zh).



Subtitle Format:





Dropdown for subtitle formats (srt, vtt, txt, json).



Translation Toggle:





Checkbox for translating subtitles to English.



Output Path:





Input field for selecting output directory (default: ~/Downloads) or generating download links for web-based results.



Progress and Status:





Progress bar (indeterminate for ongoing tasks, determinate if percentage available).



Status messages (e.g., "Loading AI model...", "Downloading video...").



Log Display:





Scrollable log area for detailed processing information (e.g., "Extracting audio...", "Transcription completed").



Buttons:





"Load AI Model" for initializing the Whisper model.



"Generate Subtitles" for processing local videos.



"Load Video & Get Qualities" for retrieving YouTube video information.



"Download Video" for downloading YouTube videos.



"Download Subtitles Only" for downloading YouTube subtitles without video.



"Clear" to reset input fields and logs.

Code Quality





ESLint: Use the configured ESLint rules in the Vite project for consistent code quality.



TypeScript: Optionally integrate TypeScript for type safety (see README.md for TypeScript setup instructions).



Error Handling: Display user-friendly error messages using modals or alerts (e.g., react-toastify or custom components).



Accessibility: Ensure UI components are accessible (ARIA attributes, keyboard navigation).

File Structure





Place React components in src/components/.



Place utility functions in src/utils/.



Place API-related code in src/api/.



Place styles in src/styles/ or use Tailwind CSS classes directly in components.

Example Component Structure





VideoInput.js: Handles video file upload and YouTube URL input.



ModelSelector.js: Dropdown for AI model selection with info tooltips.



LanguageSelector.js: Dropdown for language selection.



SubtitleFormatSelector.js: Dropdown for subtitle format selection.



TranslationToggle.js: Checkbox for English translation.



OutputPathSelector.js: Input for output path or download link.



ProgressBar.js: Displays processing progress.



LogDisplay.js: Scrollable log area for processing details.



ActionButtons.js: Contains buttons for loading model, generating subtitles, downloading, etc.

Integration Notes





Ensure the frontend sends correct parameters to the backend API based on the Python scripts (subs.py, youtube_downloader.py).



Handle backend responses (e.g., video info, subtitle files, download paths) and display them appropriately.



Match the backend's supported formats, languages, and options to avoid mismatches.

Additional Notes





Avoid hardcoding backend URLs; use environment variables (e.g., .env with VITE_API_URL).



Test the UI with mock API responses before backend integration.



Ensure the UI gracefully handles backend errors and network issues.