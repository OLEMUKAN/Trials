#!/usr/bin/env python3
"""
AI Video Subtitle Generator
Extracts audio from video and generates accurate English subtitles using OpenAI Whisper
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import sys
import subprocess
import json
import tempfile
from datetime import timedelta
import wave
import contextlib

# Install packages from requirements.txt if needed
def install_requirements():
    """Install packages from requirements.txt if not already installed"""
    import subprocess, sys, os
    req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(req_file):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
        except Exception as e:
            print(f"Error installing requirements: {e}")

# Install requirements if needed
install_requirements()

import whisper
from moviepy.editor import VideoFileClip
from pydub import AudioSegment


class AISubtitleGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Video Subtitle Generator")
        self.root.geometry("900x700")
        self.root.configure(bg='#2b2b2b')
        
        # Variables
        self.video_path = tk.StringVar()
        self.output_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))
        self.model_size = tk.StringVar(value="base")
        self.language = tk.StringVar(value="zh")  # Default to Chinese
        self.subtitle_format = tk.StringVar(value="srt")
        self.translate_to_english = tk.BooleanVar(value=False)
        self.current_model = None
        
        # Supported video formats
        self.supported_formats = [
            '.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm', '.mpg', '.mpeg',
            '.m4v', '.3gp', '.ogv', '.ts', '.mts', '.m2ts'
        ]
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors for dark theme
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground='#ffffff', background='#2b2b2b')
        style.configure('TLabel', foreground='#ffffff', background='#2b2b2b')
        style.configure('TButton', font=('Arial', 10))
        style.configure('TEntry', font=('Arial', 10))
        style.configure('TCombobox', font=('Arial', 10))
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="AI Video Subtitle Generator", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Video File Selection
        ttk.Label(main_frame, text="Video File:").grid(row=1, column=0, sticky=tk.W, pady=5)
        video_entry = ttk.Entry(main_frame, textvariable=self.video_path, width=60)
        video_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        browse_video_btn = ttk.Button(main_frame, text="Browse Video", command=self.browse_video)
        browse_video_btn.grid(row=1, column=2, padx=(5, 0), pady=5)
        
        # Model Size Selection
        ttk.Label(main_frame, text="AI Model Size:").grid(row=2, column=0, sticky=tk.W, pady=5)
        model_combo = ttk.Combobox(main_frame, textvariable=self.model_size, 
                                  values=["tiny", "base", "small", "medium", "large"], 
                                  state="readonly", width=20)
        model_combo.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Model info label
        self.model_info_label = ttk.Label(main_frame, text="Base model: Good balance of speed and accuracy", 
                                         font=('Arial', 9), foreground='#cccccc')
        self.model_info_label.grid(row=2, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # Language Selection
        ttk.Label(main_frame, text="Language:").grid(row=3, column=0, sticky=tk.W, pady=5)
        language_combo = ttk.Combobox(main_frame, textvariable=self.language,
                                     values=["zh", "en", "auto", "es", "fr", "de", "it", "pt", "ru", "ja", "ko"],
                                     state="readonly", width=20)
        language_combo.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Language info label
        self.language_info_label = ttk.Label(main_frame, text="Chinese (Mandarin/Cantonese) - Excellent accuracy", 
                                           font=('Arial', 9), foreground='#cccccc')
        self.language_info_label.grid(row=3, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # Translation Option
        translate_check = ttk.Checkbutton(main_frame, text="Translate to English", 
                                         variable=self.translate_to_english)
        translate_check.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Subtitle Format Selection
        ttk.Label(main_frame, text="Subtitle Format:").grid(row=5, column=0, sticky=tk.W, pady=5)
        format_combo = ttk.Combobox(main_frame, textvariable=self.subtitle_format,
                                   values=["srt", "vtt", "txt", "json"], 
                                   state="readonly", width=20)
        format_combo.grid(row=5, column=1, sticky=tk.W, pady=5)
        
        # Output Path
        ttk.Label(main_frame, text="Output Path:").grid(row=6, column=0, sticky=tk.W, pady=5)
        output_entry = ttk.Entry(main_frame, textvariable=self.output_path, width=60)
        output_entry.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=5)
        
        browse_output_btn = ttk.Button(main_frame, text="Browse", command=self.browse_output)
        browse_output_btn.grid(row=6, column=2, padx=(5, 0), pady=5)
        
        # Buttons Frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=7, column=0, columnspan=3, pady=20)
        
        # Load Model Button
        load_model_btn = ttk.Button(buttons_frame, text="Load AI Model", command=self.load_model)
        load_model_btn.pack(side=tk.LEFT, padx=5)
        
        # Generate Subtitles Button
        generate_btn = ttk.Button(buttons_frame, text="Generate Subtitles", command=self.generate_subtitles)
        generate_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear Button
        clear_btn = ttk.Button(buttons_frame, text="Clear", command=self.clear_fields)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # Status Label
        self.status_label = ttk.Label(main_frame, text="Ready - Select a video file to begin")
        self.status_label.grid(row=8, column=0, columnspan=3, pady=5)
        
        # Log Text Area
        ttk.Label(main_frame, text="Processing Log:").grid(row=9, column=0, sticky=tk.W, pady=(10, 5))
        self.log_text = scrolledtext.ScrolledText(main_frame, height=20, width=90, 
                                                 bg='#1e1e1e', fg='#ffffff', 
                                                 insertbackground='#ffffff')
        self.log_text.grid(row=10, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(10, weight=1)
        
        # Bind model size change
        model_combo.bind('<<ComboboxSelected>>', self.update_model_info)
        
    def log_message(self, message):
        """Add message to log text area"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def update_status(self, status):
        """Update status label"""
        self.status_label.config(text=status)
        self.root.update_idletasks()
        
    def update_model_info(self, event=None):
        """Update model information based on selection"""
        model_info = {
            "tiny": "Tiny: Fastest, least accurate (~39 MB)",
            "base": "Base: Good balance of speed and accuracy (~74 MB)",
            "small": "Small: Better accuracy, slower (~244 MB)",
            "medium": "Medium: High accuracy, slower (~769 MB)",
            "large": "Large: Best accuracy, slowest (~1550 MB)"
        }
        self.model_info_label.config(text=model_info.get(self.model_size.get(), ""))
        
    def browse_video(self):
        """Browse for video file"""
        # Create the file type string from the supported formats list
        video_patterns = " ".join([f"*{ext}" for ext in self.supported_formats])
        file_types = [
            ("Video files", video_patterns),
            ("All files", "*.*")
        ]
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=file_types
        )
        
        if file_path:
            self.video_path.set(file_path)
            self.log_message(f"Selected video: {os.path.basename(file_path)}")
            
    def browse_output(self):
        """Browse for output folder"""
        folder = filedialog.askdirectory(initialdir=self.output_path.get())
        if folder:
            self.output_path.set(folder)
            
    def clear_fields(self):
        """Clear all input fields"""
        self.video_path.set("")
        self.log_text.delete(1.0, tk.END)
        self.update_status("Ready - Select a video file to begin")
        
    def validate_video_file(self, file_path):
        """Validate video file"""
        if not os.path.exists(file_path):
            return False, "Video file does not exist"
            
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext not in self.supported_formats:
            return False, f"Unsupported video format: {file_ext}"
            
        return True, "Valid video file"
        
    def load_model(self):
        """Load the Whisper model"""
        threading.Thread(target=self._load_model_thread, daemon=True).start()
        
    def _load_model_thread(self):
        """Thread function to load Whisper model"""
        try:
            self.progress.start()
            self.update_status("Loading AI model...")
            
            model_size = self.model_size.get()
            self.log_message(f"Loading Whisper model: {model_size}")
            self.log_message("This may take a few minutes for the first time...")
            
            # Load the model
            self.current_model = whisper.load_model(model_size)
            
            self.log_message(f"✅ Model '{model_size}' loaded successfully!")
            self.update_status(f"Model '{model_size}' loaded and ready")
            
        except Exception as e:
            error_msg = f"❌ Error loading model: {str(e)}"
            self.log_message(error_msg)
            self.update_status("Error loading model")
            messagebox.showerror("Error", error_msg)
        finally:
            self.progress.stop()
            
    def generate_subtitles(self):
        """Generate subtitles from video"""
        video_path = self.video_path.get().strip()
        if not video_path:
            messagebox.showerror("Error", "Please select a video file")
            return
            
        # Validate video file
        is_valid, message = self.validate_video_file(video_path)
        if not is_valid:
            messagebox.showerror("Error", message)
            return
            
        if not os.path.exists(self.output_path.get()):
            messagebox.showerror("Error", "Output path does not exist")
            return
            
        # Check if model is loaded
        if self.current_model is None:
            messagebox.showerror("Error", "Please load the AI model first")
            return
            
        # Run in separate thread
        threading.Thread(target=self._generate_subtitles_thread, args=(video_path,), daemon=True).start()
        
    def _generate_subtitles_thread(self, video_path):
        """Thread function to generate subtitles"""
        temp_audio_path = None
        try:
            self.progress.start()
            self.update_status("Extracting audio from video...")
            
            # Extract audio from video
            self.log_message("=" * 60)
            self.log_message("STARTING SUBTITLE GENERATION")
            self.log_message("=" * 60)
            self.log_message(f"Video: {os.path.basename(video_path)}")
            self.log_message(f"Model: {self.model_size.get()}")
            self.log_message(f"Language: {self.language.get()}")
            self.log_message(f"Format: {self.subtitle_format.get()}")
            self.log_message("")
            
            # Create temporary audio file
            temp_audio_path = self.extract_audio(video_path)
            
            self.update_status("Running AI transcription...")
            self.log_message("🤖 Running AI transcription...")
            
            # Transcribe audio using Whisper
            result = self.current_model.transcribe(
                temp_audio_path,
                language=self.language.get() if self.language.get() != "auto" else None,
                verbose=False
            )
            
            self.log_message(f"✅ Transcription completed!")
            self.log_message(f"📊 Detected language: {result.get('language', 'unknown')}")
            self.log_message(f"📝 Total segments: {len(result.get('segments', []))}")
            
            # Generate output filename
            video_name = os.path.splitext(os.path.basename(video_path))[0]
            output_filename = f"{video_name}_subtitles.{self.subtitle_format.get()}"
            output_path = os.path.join(self.output_path.get(), output_filename)
            
            # Save subtitles in requested format
            self.save_subtitles(result, output_path)
            
            self.log_message(f"✅ Subtitles saved to: {output_path}")
            self.update_status("Subtitle generation completed!")
            
            # Show completion message
            messagebox.showinfo("Success", 
                              f"Subtitles generated successfully!\n\nSaved to: {output_path}")
            
        except Exception as e:
            error_msg = f"❌ Error generating subtitles: {str(e)}"
            self.log_message(error_msg)
            self.update_status("Error generating subtitles")
            messagebox.showerror("Error", error_msg)
        finally:
            # Clean up temporary file
            if temp_audio_path and os.path.exists(temp_audio_path):
                try:
                    os.remove(temp_audio_path)
                    self.log_message("🧹 Temporary audio file cleaned up")
                except:
                    pass
            self.progress.stop()
            
    def extract_audio(self, video_path):
        """Extract audio from video file"""
        try:
            self.log_message("🎵 Extracting audio from video...")
            
            # Create temporary audio file
            temp_audio_path = tempfile.mktemp(suffix=".wav")
            
            # Extract audio using moviepy
            video = VideoFileClip(video_path)
            audio = video.audio
            
            # Write audio to temporary file
            audio.write_audiofile(temp_audio_path, verbose=False, logger=None)
            
            # Clean up
            audio.close()
            video.close()
            
            self.log_message(f"✅ Audio extracted to temporary file")
            
            return temp_audio_path
            
        except Exception as e:
            raise Exception(f"Failed to extract audio: {str(e)}")
            
    def save_subtitles(self, result, output_path):
        """Save subtitles in the requested format"""
        subtitle_format = self.subtitle_format.get()
        
        if subtitle_format == "srt":
            self.save_srt(result, output_path)
        elif subtitle_format == "vtt":
            self.save_vtt(result, output_path)
        elif subtitle_format == "txt":
            self.save_txt(result, output_path)
        elif subtitle_format == "json":
            self.save_json(result, output_path)
        else:
            raise ValueError(f"Unsupported subtitle format: {subtitle_format}")
            
    def save_srt(self, result, output_path):
        """Save subtitles in SRT format"""
        with open(output_path, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(result['segments'], 1):
                start_time = self.seconds_to_srt_time(segment['start'])
                end_time = self.seconds_to_srt_time(segment['end'])
                text = segment['text'].strip()
                
                f.write(f"{i}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"{text}\n\n")
                
    def save_vtt(self, result, output_path):
        """Save subtitles in VTT format"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("WEBVTT\n\n")
            
            for segment in result['segments']:
                start_time = self.seconds_to_vtt_time(segment['start'])
                end_time = self.seconds_to_vtt_time(segment['end'])
                text = segment['text'].strip()
                
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"{text}\n\n")
                
    def save_txt(self, result, output_path):
        """Save subtitles in plain text format"""
        with open(output_path, 'w', encoding='utf-8') as f:
            for segment in result['segments']:
                f.write(f"{segment['text'].strip()}\n")
                
    def save_json(self, result, output_path):
        """Save subtitles in JSON format"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
            
    def seconds_to_srt_time(self, seconds):
        """Convert seconds to SRT time format"""
        td = timedelta(seconds=seconds)
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        milliseconds = int((td.total_seconds() - total_seconds) * 1000)
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
        
    def seconds_to_vtt_time(self, seconds):
        """Convert seconds to VTT time format"""
        td = timedelta(seconds=seconds)
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        milliseconds = int((td.total_seconds() - total_seconds) * 1000)
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"


def main():
    """Main function"""
    root = tk.Tk()
    app = AISubtitleGenerator(root)
    
    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()