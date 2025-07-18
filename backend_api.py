from flask import Flask, request, jsonify
import logging
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/api/ping', methods=['GET'])
def ping():
    logging.info('Received /api/ping request')
    return jsonify({'message': 'Backend is running'})

# TODO: Add endpoints for video download, info, subtitles

import yt_dlp

@app.route('/api/video-info', methods=['POST'])
def video_info():
    logging.info('Received /api/video-info request')
    data = request.get_json()
    url = data.get('url')
    logging.info(f'Request data: {data}')
    if not url:
        logging.warning('Missing URL in request')
        return jsonify({'error': 'Missing URL'}), 400
    try:
        ydl_opts = {'quiet': True, 'skip_download': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        logging.info('Video info fetched successfully')
        return jsonify({'info': info})
    except Exception as e:
        logging.error(f'Error fetching video info: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
