# Crop Disease Detection and Health Assessment System

CropDoctor is a web-based computer vision application designed to detect and diagnose plant diseases from leaf imagery. The system utilizes an Ultralytics YOLO11 object detection model coupled with an OpenCV image processing pipeline to identify disease classes, localize infected areas, calculate affected leaf surface percentage, and compute an overall plant health score.

The application includes an interactive user interface built with Flask, a persistent SQLite database for scan tracking, and an automated reporting engine.

## Overview

Plant diseases represent a major factor in reduced agricultural productivity. Timely and accurate diagnosis is critical for effective intervention. This project provides a diagnostic tool that identifies common pathologies across major crops in the Solanaceae family, offering actionable treatment and prevention recommendations.

### Key Capabilities

- Real-Time Disease Detection: Deep learning inference using YOLO11 fine-tuned on plant leaf pathology datasets.
- Severity Estimation: Custom computer vision pipeline that computes pixel-level infected area versus total leaf surface area.
- Plant Health Scoring: Weighted scoring algorithm that balances infection severity, pathogen risk, and lesion count on a 0 to 100 scale.
- Actionable Recommendations: Integrated database providing organic and chemical treatments, causal organism details, and preventive farming practices.
- Diagnostic History and Reporting: Tracks historical scans with filtering, time-series progression, and print-ready PDF/diagnostic report sheets.
- User Management: Session-based authentication and profile management backed by SQLite.

## Supported Crops and Pathologies

The system is trained to identify 15 distinct health conditions across three key crops:

### 1. Tomato (Solanum lycopersicum)
- Bacterial Spot (Xanthomonas spp.)
- Early Blight (Alternaria linariae)
- Late Blight (Phytophthora infestans)
- Leaf Mold (Passalora fulva)
- Septoria Leaf Spot (Septoria lycopersici)
- Spider Mites (Tetranychus urticae)
- Target Spot (Corynespora cassiicola)
- Tomato Yellow Leaf Curl Virus (TYLCV)
- Tomato Mosaic Virus (ToMV)
- Healthy (Uninfected)

### 2. Potato (Solanum tuberosum)
- Early Blight (Alternaria solani)
- Late Blight (Phytophthora infestans)
- Healthy (Uninfected)

### 3. Bell Pepper (Capsicum annuum)
- Bacterial Spot (Xanthomonas campestris pv. vesicatoria)
- Healthy (Uninfected)

## Technology Stack

- Backend: Python 3.10+, Flask
- Computer Vision and Deep Learning: Ultralytics YOLO11, OpenCV, NumPy
- Database: SQLite3
- Security: Bcrypt password hashing
- Frontend: HTML5, CSS3, Vanilla JavaScript, Chart.js

## Project Structure

```text
Crop-Disease-Detector/
├── CropDoctor/
│   ├── models/
│   │   └── best.pt               # Fine-tuned YOLO11 model weights
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css         # Application stylesheet
│   │   ├── js/
│   │   │   └── app.js            # Client-side application logic
│   │   └── uploads/              # Stored original and annotated images
│   ├── templates/
│   │   └── index.html            # Single-page interface template
│   ├── app.py                    # Flask server and API endpoints
│   ├── recommendations.py        # Agronomic pathology database
│   ├── requirements.txt          # Python dependencies
│   └── train_model.py            # YOLO training configuration script
├── .gitignore                    # Excludes datasets, cache, and virtual environment
└── README.md                     # Project documentation
```

## Installation and Setup

### Prerequisites

- Python 3.10 or higher
- Git installed on your system

### 1. Clone the Repository

```bash
git clone https://github.com/kasturimanna/Crop-Disease-Detector.git
cd Crop-Disease-Detector
```

### 2. Set Up Virtual Environment

It is recommended to run the project within an isolated virtual environment.

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On Linux or macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

Navigate to the application folder and install dependencies:

```bash
cd CropDoctor
pip install -r requirements.txt
```

### 4. Run the Application

Start the Flask application server:

```bash
python app.py
```

Once initialized, open your web browser and navigate to:
```text
http://localhost:8000
```

### 5. Default Credentials

For initial testing, an administrative account is seeded automatically:
- Email: admin@cropdoctor.ai
- Password: admin123

New users can also register accounts directly on the interface.

## Model Details and Methodology

- Architecture: Ultralytics YOLO11 Nano (yolo11n)
- Input Resolution: 256x256 pixels
- Model Size: Approximately 5.4 MB
- Task: Bounding box object detection and class categorization
- Severity Pipeline: Threshold-based segmentation isolates the leaf boundary from background noise. HSV color masking then calculates the ratio of necrotic/chlorotic pixels within localized bounding boxes relative to total leaf area.

## License

This project is developed for academic and educational evaluation. All rights reserved.
