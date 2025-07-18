import React from 'react';

const ActionButton = ({ onClick, disabled, children, className }) => (
  <button
    onClick={onClick}
    className={`w-full px-4 py-3 bg-gray-700 text-white rounded-lg hover:bg-gray-600 disabled:bg-gray-800 disabled:text-gray-500 transition-colors duration-200 ease-in-out ${className}`}
    disabled={disabled}
  >
    {children}
  </button>
);

const ActionButtons = ({
  onGenerateSubtitles,
  onLoadVideoInfo,
  onDownloadVideo,
  onDownloadSubtitles,
  onClear,
  loading
}) => (
  <div className="grid grid-cols-2 gap-4 mb-6">
    <ActionButton onClick={onGenerateSubtitles} disabled={loading} className="bg-blue-600 hover:bg-blue-700 col-span-2">
      Generate Subtitles
    </ActionButton>
    <ActionButton onClick={onLoadVideoInfo} disabled={loading} className="bg-purple-600 hover:bg-purple-700">
      Load Video Info
    </ActionButton>
    <ActionButton onClick={onDownloadVideo} disabled={loading} className="bg-yellow-600 hover:bg-yellow-700">
      Download Video
    </ActionButton>
    <ActionButton onClick={onDownloadSubtitles} disabled={loading} className="bg-pink-600 hover:bg-pink-700 col-span-2">
      Download Subtitles Only
    </ActionButton>
    <ActionButton onClick={onClear} disabled={loading} className="bg-red-600 hover:bg-red-700 col-span-2">
      Clear All
    </ActionButton>
  </div>
);

export default ActionButtons;
