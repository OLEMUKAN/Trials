import React, { useEffect, useRef } from 'react';

const LogDisplay = ({ logs }) => {
  const logEndRef = useRef(null);

  useEffect(() => {
    logEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [logs]);

  return (
    <div className="mt-4 p-4 bg-gray-900 rounded-lg h-64 overflow-y-auto text-sm text-gray-300 font-mono">
      {logs.length === 0 ? (
        <span className="text-gray-500">Awaiting actions...</span>
      ) : (
        logs.map((log, idx) => <div key={idx} className="whitespace-pre-wrap">{`[${new Date().toLocaleTimeString()}] ${log}`}</div>)
      )}
      <div ref={logEndRef} />
    </div>
  );
};

export default LogDisplay;
