import React from 'react';

const OutputPathSelector = ({ value, onChange }) => (
  <div className="mb-4">
    <label className="block text-gray-300 font-semibold mb-2">Output Path</label>
    <input
      type="text"
      value={value}
      onChange={e => onChange(e.target.value)}
      placeholder="e.g. ~/Downloads or leave blank for default"
      className="w-full p-3 rounded-lg bg-gray-700 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-blue-500 focus:outline-none"
    />
  </div>
);

export default OutputPathSelector;
