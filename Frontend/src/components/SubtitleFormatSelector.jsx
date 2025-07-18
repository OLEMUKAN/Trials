import React from 'react';

const SUBTITLE_FORMATS = [
  { value: 'srt', label: 'SRT' },
  { value: 'vtt', label: 'VTT' },
  { value: 'txt', label: 'Text' },
  { value: 'json', label: 'JSON' },
];

const SubtitleFormatSelector = ({ value, onChange }) => (
  <div className="mb-6 p-4 bg-gray-800 rounded-lg shadow">
    <label className="block text-white font-semibold mb-2">Subtitle Format</label>
    <select
      value={value}
      onChange={e => onChange(e.target.value)}
      className="w-full p-2 rounded bg-gray-700 text-gray-200 border border-gray-600"
    >
      {SUBTITLE_FORMATS.map(fmt => (
        <option key={fmt.value} value={fmt.value}>{fmt.label}</option>
      ))}
    </select>
  </div>
);

export default SubtitleFormatSelector;
