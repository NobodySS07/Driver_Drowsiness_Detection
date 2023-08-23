# Driver Drowsiness Detection System


![ezgif com-video-to-gif](https://github.com/NobodySS07/Driver_Drowsiness_Detection/assets/60501204/bf5dd603-dbf7-4e7f-a598-2678338e7f4e)


This repository contains code for a Driver Drowsiness Detection System that uses computer vision techniques and deep learning models to detect drowsiness in drivers.

## System Flow

1. **Dash Cam Video Capture:** The system captures the driver's video feed using a dash cam.

2. **Video to Frames:** OpenCV is used to extract frames from the video stream. Each frame is treated as an individual image.

3. **Face Detection:** The extracted frames are processed through a pre-trained ResNet .caffemodel for face detection using OpenCV. This detects and localizes faces in the frames.

4. **Cropped Faces:** The faces detected in the frames are cropped and isolated as individual face images.

5. **Drowsiness Classification:** The cropped face images are passed through a VGG16-based image classification model. This model was trained on a diverse dataset containing approximately 9000 images with drowsy and non-drowsy labels. The model predicts whether the driver's face is showing signs of drowsiness or not.

6. **Performance Enhancement:** Initially, the VGG16 model achieved an accuracy of 85%. However, by using cropped face images, the performance was significantly improved, achieving almost 100% accuracy.

7. **Real-time Processing:** The entire system operates in real-time, with a processing speed of approximately 17 frames per second on a 20 frames per second video feed when running on a CPU.

## Dataset

The VGG16-based image classification model was trained on a multiracial dataset sourced from Kaggle. The dataset contains around 9000 images, each labeled as Active and Fatigue Subjects.

[Link to Dataset](https://www.kaggle.com/datasets/rakibuleceruet/drowsiness-prediction-dataset)

## VGG16-based image classification model

[Link to Model](https://drive.google.com/file/d/1zyOEzHi1LVrZCeqVdtF9yn7ARYQrtsOt/view?usp=drive_link)
## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/driver-drowsiness-detection.git
2. Download my_model.h5 from the given link and paste it in root folder. 
3. Install the required dependencies. You can use pip to install them:
   ```bash
   pip install -r requirements.txt
4. Run the main script to start the drowsiness detection system:
   ```bash
   python main.py
