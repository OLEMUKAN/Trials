import React from 'react';

const ProgressBar = ({ progress, indeterminate }) => (
  <div className="w-full h-4 bg-gray-700 rounded mb-6">
    <div
      className={`h-4 rounded ${indeterminate ? 'animate-pulse bg-blue-600 w-full' : 'bg-blue-600'}`}
      style={!indeterminate ? { width: `${progress}%` } : {}}
    />
  </div>
);

export default ProgressBar;
