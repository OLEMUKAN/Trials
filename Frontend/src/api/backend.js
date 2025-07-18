// src/api/backend.js
// Utility functions to interact with the Python backend API

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

export async function uploadVideo(file) {
  const formData = new FormData();
  formData.append('video', file);
  const res = await fetch(`${API_URL}/upload`, {
    method: 'POST',
    body: formData,
  });
  return res.json();
}



export async function getYoutubeInfo(url) {
  console.log('Sending request to backend:', { url });
  const res = await fetch(`${API_URL}/api/video-info`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url }),
  });
  const data = await res.json();
  console.log('Received response from backend:', data);
  return data;
}

export async function downloadYoutubeVideo(url, quality) {
  const res = await fetch(`${API_URL}/youtube/download`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url, quality }),
  });
  return res.json();
}

export async function generateSubtitles(params) {
  const res = await fetch(`${API_URL}/subtitles/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(params),
  });
  return res.json();
}

export async function getLogs(taskId) {
  const res = await fetch(`${API_URL}/logs/${taskId}`);
  return res.json();
}
