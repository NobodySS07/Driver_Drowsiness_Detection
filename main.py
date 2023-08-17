import warnings
warnings.filterwarnings("ignore")
from PIL import Image
import cv2
from keras.models import load_model
import numpy as np
import tensorflow as tf
from keras.preprocessing import image

class DrowsinessClassifier:
    def __init__(self):
        self.model = load_model('my_model.h5',compile=False)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def face_extractor(self, img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image
        faces = self.face_cascade.detectMultiScale(img, 1.3, 5)
    
        if faces is ():
            return None
    
        # Crop all faces found
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face
    
    def per_frame(self, cv, frame):
        face=self.face_extractor(frame)
        if type(face) is np.ndarray:
            face = cv.resize(face, (224, 224))
            im = Image.fromarray(face, 'RGB')
            img_array = np.array(im) 
            img_array = np.expand_dims(img_array, axis=0)
            pred = self.model.predict(img_array)
            # classes = np.argmax(pred,axis=1)
            # print('Here ',classes)
            # print(pred)       
            name="None matching"
            if(pred[0] < 0.9):
                name='Awake'
                cv.putText(frame,name, (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            elif(pred[0] >=0.9):
                name='Drowsy'
                cv.putText(frame,name, (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        else:
            cv.putText(frame,"No face found", (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    

classifier = DrowsinessClassifier()
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    classifier.per_frame(cv2, frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break