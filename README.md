# Driver Drowsiness Detection System

![Demo](demo.gif)

## Overview

This repository contains the implementation of a Driver Drowsiness Detection System using computer vision techniques. The system captures video from a webcam, processes it through various stages, and predicts whether the driver is drowsy or not based on facial features. The flow of the system is as follows:

1. **Webcam Input:** Captures live video stream from the webcam.
2. **Video to Frames:** Converts the video stream into individual frames using OpenCV.
3. **Face Detection:** Utilizes OpenCV's ResNet-based `.caffemodel` to detect faces in the frames.
4. **Cropped Faces:** Extracts cropped face images from the frames.
5. **Drowsiness Classification:** Employs a VGG16-based image classification model to predict drowsiness or alertness.
6. **Result:** The system outputs real-time drowsiness alerts based on the predictions.

## Dataset

The VGG16 model used in this system was trained on a multiracial dataset obtained from Kaggle. The dataset consists of approximately 9000 images categorized as drowsy and non-drowsy images.

**Dataset Link:** [Add Dataset Link Here]

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Other necessary libraries (Numpy, etc.)

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/drowsiness-detection.git
   cd drowsiness-detection
