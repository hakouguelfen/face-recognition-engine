# Face Recognition Engine
A machine learning-powered backend for real-time facial detection and recognition, using Convolutional Neural Networks (CNN). This repository focuses on training, learning, and prediction processes for detecting faces in images, designed as the backend for a full facial detection app.

## Features
* CNN-based model for facial detection
* Real-time face detection and recognition
* Preprocessing of input images for better accuracy
* Supports integration with front-end applications via API
* High accuracy for facial recognition tasks

## Installation
1. Clone the repository:
```bash
git clone https://github.com/hakouguelfen/face-recognition-engine.git
cd face-recognition-engine
```

2. Ensure you have Python 3.7+ installed:
```bash
python --version
```

3. Create virtual env
```bash
python3 -m venv env
```

4. Activate virtual env
```bash
source env/bin/activate
```
for windows
```bash
.\env\Scripts\activate
```

5. Install required dependencies:

```bash
pip install -r requirements.txt
```

### Using Docker
build docker image
```bash
docker build -t face-recognition .
```

run docker image
```bash
docker run -d -p 3000:3000 -v $(pwd):/app --name myapp face-recognition
```

### Dependencies include:
 * pytest
 * pytest-cov (for coverage reports)
 * scikit-learn (for machine learning algorithms)
 * Flask (for http requests)
 * face_recognition (for extracting facial encodings)

## Usage
### Command Line Interface
```bash
python facial_detection/main.py
```

### Exposed endpoints 
* save_face
```bash
curl -X POST \
  -F "image=@/path/image.jpg" \
  -F "label=Person name" \
  http://localhost:3000/save_face
```

* predict
```bash
curl -X POST \
  -F "image=@/path/image.jpg" \
  http://localhost:3000/predict
```

## Testing

### Running Tests
Run the entire test suite:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov
```

Run specific test file:
```bash
pytest tests/test_.py
```


## Acknowledgments
* Python community resources
* pytest documentation and community
