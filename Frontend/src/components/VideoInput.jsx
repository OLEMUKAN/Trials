import React, { useState } from 'react';

const VideoInput = ({ onVideoSelect, onUrlInput }) => {
  const [url, setUrl] = useState('');

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      onVideoSelect(e.target.files[0]);
    }
  };

  const handleUrlChange = (e) => {
    setUrl(e.target.value);
  };

  const handlePasteUrl = () => {
    if (url.trim()) {
      onUrlInput(url.trim());
    }
  };

  return (
    <div className="mb-4">
      <div>
        <label className="block text-gray-300 font-semibold mb-2">Video File Upload</label>
        <input
          type="file"
          accept="video/*"
          className="block w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-600 file:text-white hover:file:bg-blue-700"
          onChange={handleFileChange}
        />
      </div>
      <div className="mt-4">
        <label className="block text-gray-300 font-semibold mb-2">Or Paste YouTube URL</label>
        <div className="flex">
          <input
            type="text"
            value={url}
            onChange={handleUrlChange}
            placeholder="https://www.youtube.com/watch?v=..."
            className="flex-1 p-3 rounded-l-lg bg-gray-700 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-blue-500 focus:outline-none"
          />
          <button
            onClick={handlePasteUrl}
            className="px-4 py-2 bg-blue-600 text-white rounded-r-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Load
          </button>
        </div>
      </div>
    </div>
  );
};

export default VideoInput;
