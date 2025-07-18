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
    <div className="mb-6 p-4 bg-gray-800 rounded-lg shadow">
      <label className="block text-white font-semibold mb-2">Video File Upload</label>
      <input
        type="file"
        accept="video/*"
        className="block w-full text-gray-200 bg-gray-700 border border-gray-600 rounded p-2 mb-4"
        onChange={handleFileChange}
      />
      <label className="block text-white font-semibold mb-2">Or Paste YouTube URL</label>
      <div className="flex">
        <input
          type="text"
          value={url}
          onChange={handleUrlChange}
          placeholder="Paste YouTube link here..."
          className="flex-1 p-2 rounded-l bg-gray-700 text-gray-200 border border-gray-600"
        />
        <button
          onClick={handlePasteUrl}
          className="px-4 py-2 bg-blue-600 text-white rounded-r hover:bg-blue-700"
        >
          Load
        </button>
      </div>
    </div>
  );
};

export default VideoInput;
