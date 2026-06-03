"""
Module: pose_engine.py
Description: AI IP Core using OpenCV DNN and pre-trained MobileNet-SSD.
"""
import cv2
import numpy as np

class PoseEngine:
    def __init__(self):
        print("AI Engine: Loading Pre-built Deep Learning Model (MobileNet-SSD)...")
        self.net = cv2.dnn.readNetFromCaffe(
            'MobileNetSSD_deploy.prototxt', 
            'MobileNetSSD_deploy.caffemodel'
        )

    def process_frame(self, frame):
        h, w = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        self.net.setInput(blob)
        detections = self.net.forward()
        
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            class_id = int(detections[0, 0, i, 1])
            
            if class_id == 15 and confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                return {'w': endX - startX, 'h': endY - startY}
                
        return None
