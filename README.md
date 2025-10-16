# Python-text-extraction-from-images
# Image Text Extractor (OCR)

A full-stack web application that extracts text from images using Optical Character Recognition (OCR). Built with Python Flask backend and modern HTML/CSS/JavaScript frontend.

## Features

- 🖼️ Upload images in JPG, PNG, GIF, BMP formats
- 📄 Extract text using Tesseract OCR
- 🎯 Drag-and-drop image upload
- 📋 Copy extracted text to clipboard
- 🚀 Fast and efficient processing
- 💻 Responsive web interface
- 🔧 RESTful API backend

## Screenshots

Upload Interface → Text Extraction → Copy & Download Results

## Tech Stack

**Backend:**
- Python 3.7+
- Flask (Web framework)
- Flask-CORS (Cross-origin requests)
- Pillow (Image processing)
- Pytesseract (OCR engine)

**Frontend:**
- HTML5
- CSS3 (Modern styling)
- JavaScript (Vanilla JS)

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Tesseract OCR engine

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/image-text-extractor.git
cd image-text-extractor
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

**Windows:**
- Download installer: https://github.com/UB-Mannheim/tesseract/wiki
- Run the installer (default path: `C:\Program Files\Tesseract-OCR`)
- If installed in custom location, update `backend.py`:
  ```python
  pytesseract.pytesseract.pytesseract_cmd = r'your\path\to\tesseract.exe'
  ```

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

**Linux (Fedora/RHEL):**
```bash
sudo yum install tesseract
```

## Project Structure

```
image-text-extractor/
├── backend.py              # Flask API server
├── frontend.py             # Flask frontend server
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web UI


## Usage

### 1. Start the Backend Server

Open Terminal 1:

```bash
python backend.py
```

You should see:
```
 * Running on http://localhost:5000
```

### 2. Start the Frontend Server

Open Terminal 2:

```bash
python frontend.py
```

You should see:
```
 * Running on http://localhost:8000
```

### 3. Open in Browser

Navigate to: **http://localhost:8000**

### 4. Extract Text

1. Upload an image by clicking or drag-dropping
2. Wait for text extraction to complete
3. Copy extracted text or upload another image

## API Endpoints

### Extract Text from Image

**POST** `/api/extract-text`

**Request:**
```bash
curl -X POST -F "image=@image.jpg" http://localhost:5000/api/extract-text
```

**Response:**
```json
{
  "success": true,
  "text": "Extracted text from image...",
  "filename": "image.jpg"
}
```

### Health Check

**GET** `/api/health`

**Response:**
```json
{
  "status": "Backend is running"
}
```

## Configuration

### Backend (backend.py)
- **Port:** 5000
- **Debug:** True (disable in production)
- **Max File Size:** 16MB
- **Allowed Formats:** JPG, JPEG, PNG, GIF, BMP

### Frontend (frontend.py)
- **Port:** 8000
- **Proxy to Backend:** http://localhost:5000

## Troubleshooting

### ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Tesseract not found
- Verify Tesseract is installed on your system
- Windows users: Check installation path in `backend.py`
- Run: `tesseract --version` to verify

### Port already in use
Change the port in the respective `.py` file:
```python
app.run(host='localhost', port=9000)  # Change 9000 to any free port
