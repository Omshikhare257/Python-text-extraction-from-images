from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__, template_folder='templates')

BACKEND_URL = 'http://localhost:5000'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Forward request to backend
        files = {'image': (file.filename, file.stream, file.content_type)}
        response = requests.post(f'{BACKEND_URL}/api/extract-text', files=files)
        
        return response.json(), response.status_code
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    try:
        response = requests.get(f'{BACKEND_URL}/api/health')
        return jsonify({'status': 'Frontend connected to backend'}), 200
    except:
        return jsonify({'status': 'Backend not available'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)