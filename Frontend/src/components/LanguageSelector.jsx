import React from 'react';

const LANGUAGES = [
  { value: 'zh', label: 'Chinese' },
  { value: 'en', label: 'English' },
  { value: 'auto', label: 'Auto Detect' },
  { value: 'es', label: 'Spanish' },
  { value: 'fr', label: 'French' },
  { value: 'de', label: 'German' },
  { value: 'it', label: 'Italian' },
  { value: 'pt', label: 'Portuguese' },
  { value: 'ru', label: 'Russian' },
  { value: 'ja', label: 'Japanese' },
  { value: 'ko', label: 'Korean' },
];

const LanguageSelector = ({ value, onChange }) => (
  <div className="mb-4">
    <label className="block text-gray-300 font-semibold mb-2">Language</label>
    <select
      value={value}
      onChange={e => onChange(e.target.value)}
      className="w-full p-3 rounded-lg bg-gray-700 text-gray-200 border border-gray-600 focus:ring-2 focus:ring-blue-500 focus:outline-none"
    >
      {LANGUAGES.map(lang => (
        <option key={lang.value} value={lang.value}>{lang.label}</option>
      ))}
    </select>
  </div>
);

export default LanguageSelector;
