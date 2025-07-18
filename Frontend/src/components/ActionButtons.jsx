import React from 'react';

const ActionButtons = ({
  onLoadModel,
  onGenerateSubtitles,
  onLoadVideoInfo,
  onDownloadVideo,
  onDownloadSubtitles,
  onClear,
  loading
}) => (
  <div className="flex flex-wrap gap-4 mb-6">
    <button
      onClick={onLoadModel}
      className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
      disabled={loading}
    >
      Load AI Model
    </button>
    <button
      onClick={onGenerateSubtitles}
      className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      disabled={loading}
    >
      Generate Subtitles
    </button>
    <button
      onClick={onLoadVideoInfo}
      className="px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700"
      disabled={loading}
    >
      Load Video & Get Qualities
    </button>
    <button
      onClick={onDownloadVideo}
      className="px-4 py-2 bg-yellow-600 text-white rounded hover:bg-yellow-700"
      disabled={loading}
    >
      Download Video
    </button>
    <button
      onClick={onDownloadSubtitles}
      className="px-4 py-2 bg-pink-600 text-white rounded hover:bg-pink-700"
      disabled={loading}
    >
      Download Subtitles Only
    </button>
    <button
      onClick={onClear}
      className="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700"
      disabled={loading}
    >
      Clear
    </button>
  </div>
);

export default ActionButtons;
