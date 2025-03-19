import cv2
import dlib
import numpy as np
import torch
from ultralytics import YOLO
import folium

# Load YOLOv8 model for animal detection
model = YOLO("yolov8n.pt")

def detect_animals(image_path):
    img = cv2.imread(image_path)
    results = model(img)
    
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = result.names[int(box.cls[0])]
            conf = box.conf[0]
            
            if conf > 0.5:
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Animal Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Face profiling using dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def face_profiling(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        
        for n in range(68):
            x, y = landmarks.part(n).x, landmarks.part(n).y
            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
    
    cv2.imshow("Face Profiling", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

