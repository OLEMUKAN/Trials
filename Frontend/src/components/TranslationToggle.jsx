import React from 'react';

const TranslationToggle = ({ checked, onChange }) => (
  <div className="mb-6 p-4 bg-gray-800 rounded-lg shadow flex items-center">
    <input
      type="checkbox"
      id="translateToEnglish"
      checked={checked}
      onChange={e => onChange(e.target.checked)}
      className="mr-2 accent-blue-600"
    />
    <label htmlFor="translateToEnglish" className="text-white font-semibold">Translate subtitles to English</label>
  </div>
);

export default TranslationToggle;
