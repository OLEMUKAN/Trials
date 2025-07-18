import React from 'react';

const SUBTITLE_FORMATS = [
  { value: 'srt', label: 'SRT' },
  { value: 'vtt', label: 'VTT' },
  { value: 'txt', label: 'Text' },
  { value: 'json', label: 'JSON' },
];

const SubtitleFormatSelector = ({ value, onChange }) => (
  <div className="mb-4">
    <label className="block text-gray-300 font-semibold mb-2">Subtitle Format</label>
    <select
      value={value}
      onChange={e => onChange(e.target.value)}
      className="w-full p-3 rounded-lg bg-gray-700 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-blue-500 focus:outline-none"
    >
      {SUBTITLE_FORMATS.map(fmt => (
        <option key={fmt.value} value={fmt.value}>{fmt.label}</option>
      ))}
    </select>
  </div>
);

export default SubtitleFormatSelector;
