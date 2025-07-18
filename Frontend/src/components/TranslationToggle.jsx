import React from 'react';

const TranslationToggle = ({ checked, onChange }) => (
  <div className="mb-4 flex items-center p-3 rounded-lg bg-gray-700">
    <input
      type="checkbox"
      id="translateToEnglish"
      checked={checked}
      onChange={e => onChange(e.target.checked)}
      className="h-5 w-5 rounded-md border-gray-500 bg-gray-600 text-blue-600 focus:ring-blue-500"
    />
    <label htmlFor="translateToEnglish" className="ml-3 text-gray-200 font-semibold">Translate subtitles to English</label>
  </div>
);

export default TranslationToggle;
