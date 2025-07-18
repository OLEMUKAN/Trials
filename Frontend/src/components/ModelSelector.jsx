import React from 'react';

const MODEL_OPTIONS = [
  { value: 'tiny', label: 'Tiny: Fastest, least accurate (~39 MB)' },
  { value: 'base', label: 'Base: Good balance of speed and accuracy (~74 MB)' },
  { value: 'small', label: 'Small: Better accuracy, slower (~244 MB)' },
  { value: 'medium', label: 'Medium: High accuracy, slower (~769 MB)' },
  { value: 'large', label: 'Large: Best accuracy, slowest (~1550 MB)' },
];

const ModelSelector = ({ value, onChange }) => (
  <div className="mb-4">
    <label className="block text-gray-300 font-semibold mb-2">AI Model Size</label>
    <select
      value={value}
      onChange={e => onChange(e.target.value)}
      className="w-full p-3 rounded-lg bg-gray-700 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-blue-500 focus:outline-none"
    >
      {MODEL_OPTIONS.map(opt => (
        <option key={opt.value} value={opt.value}>{opt.label}</option>
      ))}
    </select>
  </div>
);

export default ModelSelector;
