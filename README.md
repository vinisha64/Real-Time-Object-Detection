# Real-Time Object Detection System

## Overview

A real-time object detection application built using YOLOv5, OpenCV, PyTorch, and Tkinter for detecting objects in images and live webcam streams.

## Features

* Image Object Detection
* Real-Time Webcam Object Detection
* User-Friendly GUI
* YOLOv5 Deep Learning Model

## Technologies Used

* Python
* OpenCV
* PyTorch
* YOLOv5
* Tkinter

## Project Structure

* main_frontend.py – Welcome Screen
* object_detection_gui.py – Video Detection GUI
* object_detection_backend.py – YOLOv5 Detection Backend

## Installation

pip install -r requirements.txt

## Run

python main_frontend.py

## Screenshots

### Welcome Screen

![Welcome Screen](Welcome.png)

### Image Detection

![Image Detection](image_detection.png)

### Video Detection

![Video Detection](video_detection.png)

## How It Works

1. User launches the application.
2. User selects either Image Detection or Video Detection.
3. YOLOv5 processes the image/video frame.
4. Detected objects are highlighted with bounding boxes and labels.
5. Results are displayed through the Tkinter GUI.

## Future Enhancements

- Support for custom-trained YOLO models.
- Object counting functionality.
- Detection confidence threshold adjustment.
- Video file upload detection.
- Performance optimization for faster inference.

## Author

Vinisha Saldanha
