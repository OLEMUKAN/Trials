import React from 'react';

const OutputPathSelector = ({ value, onChange }) => (
  <div className="mb-6 p-4 bg-gray-800 rounded-lg shadow">
    <label className="block text-white font-semibold mb-2">Output Path / Download Location</label>
    <input
      type="text"
      value={value}
      onChange={e => onChange(e.target.value)}
      placeholder="e.g. ~/Downloads or leave blank for default"
      className="w-full p-2 rounded bg-gray-700 text-gray-200 border border-gray-600"
    />
  </div>
);

export default OutputPathSelector;
