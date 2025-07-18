import React from 'react';

const ProgressBar = ({ progress, indeterminate }) => (
  <div className="w-full h-2 bg-gray-700 rounded-full mb-6 overflow-hidden">
    <div
      className={`h-full rounded-full transition-all duration-300 ease-in-out ${indeterminate ? 'animate-pulse bg-blue-500 w-full' : 'bg-green-500'}`}
      style={!indeterminate ? { width: `${progress}%` } : {}}
    />
  </div>
);

export default ProgressBar;
