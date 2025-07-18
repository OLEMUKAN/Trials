import React, { useState } from 'react';
import './App.css';
import VideoInput from './components/VideoInput';
import ModelSelector from './components/ModelSelector';
import LanguageSelector from './components/LanguageSelector';
import SubtitleFormatSelector from './components/SubtitleFormatSelector';
import TranslationToggle from './components/TranslationToggle';
import OutputPathSelector from './components/OutputPathSelector';
import ProgressBar from './components/ProgressBar';
import LogDisplay from './components/LogDisplay';
import ActionButtons from './components/ActionButtons';

function App() {
  // State for all controls
  const [videoFile, setVideoFile] = useState(null);
  const [youtubeUrl, setYoutubeUrl] = useState('');
  const [modelSize, setModelSize] = useState('base');
  const [language, setLanguage] = useState('zh');
  const [subtitleFormat, setSubtitleFormat] = useState('srt');
  const [translateToEnglish, setTranslateToEnglish] = useState(false);
  const [outputPath, setOutputPath] = useState('');
  const [progress, setProgress] = useState(0);
  const [indeterminate, setIndeterminate] = useState(false);
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(false);

  // Handlers (stubbed for now)
  const handleVideoSelect = (file) => {
    setVideoFile(file);
    setLogs(logs => [...logs, `Selected video file: ${file.name}`]);
  };
  const handleUrlInput = (url) => {
    setYoutubeUrl(url);
    setLogs(logs => [...logs, `YouTube URL entered: ${url}`]);
  };
  const handleLoadModel = () => {
    setLoading(true);
    setIndeterminate(true);
    setLogs(logs => [...logs, 'Loading AI model...']);
    setTimeout(() => {
      setLoading(false);
      setIndeterminate(false);
      setLogs(logs => [...logs, 'AI model loaded!']);
    }, 2000);
  };
  const handleGenerateSubtitles = () => {
    setLoading(true);
    setIndeterminate(true);
    setLogs(logs => [...logs, 'Generating subtitles...']);
    setTimeout(() => {
      setLoading(false);
      setIndeterminate(false);
      setLogs(logs => [...logs, 'Subtitles generated!']);
    }, 3000);
  };
  const handleLoadVideoInfo = () => {
    setLogs(logs => [...logs, 'Loading video info...']);
  };
  const handleDownloadVideo = () => {
    setLogs(logs => [...logs, 'Downloading video...']);
  };
  const handleDownloadSubtitles = () => {
    setLogs(logs => [...logs, 'Downloading subtitles only...']);
  };
  const handleClear = () => {
    setVideoFile(null);
    setYoutubeUrl('');
    setModelSize('base');
    setLanguage('zh');
    setSubtitleFormat('srt');
    setTranslateToEnglish(false);
    setOutputPath('');
    setProgress(0);
    setIndeterminate(false);
    setLogs([]);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white py-8 px-4">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold mb-8 text-center">YouTube Downloader & AI Subtitle Generator</h1>
        <VideoInput onVideoSelect={handleVideoSelect} onUrlInput={handleUrlInput} />
        <ModelSelector value={modelSize} onChange={setModelSize} />
        <LanguageSelector value={language} onChange={setLanguage} />
        <TranslationToggle checked={translateToEnglish} onChange={setTranslateToEnglish} />
        <SubtitleFormatSelector value={subtitleFormat} onChange={setSubtitleFormat} />
        <OutputPathSelector value={outputPath} onChange={setOutputPath} />
        <ProgressBar progress={progress} indeterminate={indeterminate} />
        <ActionButtons
          onLoadModel={handleLoadModel}
          onGenerateSubtitles={handleGenerateSubtitles}
          onLoadVideoInfo={handleLoadVideoInfo}
          onDownloadVideo={handleDownloadVideo}
          onDownloadSubtitles={handleDownloadSubtitles}
          onClear={handleClear}
          loading={loading}
        />
        <LogDisplay logs={logs} />
      </div>
    </div>
  );
}

export default App;
