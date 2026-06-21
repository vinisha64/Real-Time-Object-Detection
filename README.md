# Real-Time Object Detection System

## Overview

The Real-Time Object Detection System is a computer vision application that detects and classifies objects in images and live webcam streams using the YOLOv5 deep learning model. The project provides a user-friendly graphical interface built with Tkinter, enabling users to perform object detection without requiring command-line interaction.

This project demonstrates the integration of Deep Learning, Computer Vision, and Desktop Application Development using Python.

---

## Features

- Image Object Detection
- Real-Time Webcam Object Detection
- Bounding Box Visualization
- Object Label Prediction
- Confidence Score Display
- User-Friendly Tkinter GUI
- YOLOv5 Pre-trained Model Integration

---

## Prerequisites

Before running the project, ensure that the following software is installed:

- Python 3.10 or above
- Git
- Webcam (for live detection)
- Virtual Environment (recommended)

---

## Tech Stack

### Programming Language
- Python

### Libraries and Frameworks
- OpenCV
- PyTorch
- YOLOv5
- Tkinter
- Pillow
- NumPy

### Tools
- VS Code
- Git
- GitHub

---

## Project Structure

```text
Real-Time-Object-Detection/

├── main_frontend.py
├── object_detection_gui.py
├── object_detection_backend.py
├── requirements.txt
├── README.md
├── Welcome.png
├── image_detection.png
└── video_detection.png
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vinisha64/Real-Time-Object-Detection.git
cd Real-Time-Object-Detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the following command:

```bash
python main_frontend.py
```

The application provides two options:

### Image Detection

- Upload an image.
- Detect objects present in the image.
- Display bounding boxes and confidence scores.

### Video Detection

- Access the webcam.
- Detect objects in real time.
- Display predictions continuously.

---

## How It Works

### Image Detection Workflow

```text
User Uploads Image
        ↓
YOLOv5 Processes Image
        ↓
Objects Detected
        ↓
Bounding Boxes Drawn
        ↓
Results Displayed
```

### Video Detection Workflow

```text
Webcam Feed
      ↓
Frame Capture
      ↓
YOLOv5 Inference
      ↓
Object Detection
      ↓
Live Display
```

---

## Model Used

### YOLOv5s

The project uses the YOLOv5s (Small) pre-trained model.

Characteristics:

- Fast inference speed
- Lightweight architecture
- Suitable for real-time applications
- Trained on the COCO dataset

The model can detect 80 common object categories including:

- Person
- Bicycle
- Car
- Motorcycle
- Dog
- Cat
- Laptop
- Chair
- Bottle
- Cell Phone

and many more.

---

## Screenshots

### Welcome Screen

![Welcome Screen](Welcome.png)

### Image Detection

![Image Detection](image_detection.png)

### Video Detection

![Video Detection](video_detection.png)

---

## Applications

- Smart Surveillance Systems
- Traffic Monitoring
- Retail Analytics
- Security Systems
- Autonomous Systems
- Educational Computer Vision Projects

---

## Future Enhancements

- Custom YOLO Model Training
- Object Counting Functionality
- Video File Detection
- Multi-Camera Support
- Cloud Deployment
- Performance Optimization using GPU
- Detection Report Generation

---

## Learning Outcomes

Through this project, the following concepts were implemented:

- Deep Learning
- Object Detection
- Computer Vision
- GUI Development
- Real-Time Video Processing
- Python Programming
- Git and GitHub Version Control

---

## Author

**Vinisha Saldanha**

GitHub: https://github.com/vinisha64

---

## License

This project is developed for educational and learning purposes.
