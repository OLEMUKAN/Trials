import React from 'react';

const LogDisplay = ({ logs }) => (
  <div className="mb-6 p-4 bg-gray-900 rounded-lg shadow h-48 overflow-y-auto text-sm text-gray-100" style={{ background: '#1e1e1e' }}>
    {logs.length === 0 ? (
      <span className="text-gray-400">No logs yet.</span>
    ) : (
      logs.map((log, idx) => <div key={idx}>{log}</div>)
    )}
  </div>
);

export default LogDisplay;
