"""
Module: pose_engine.py
Project: Edge AI Fall Detection System (JCT Mini-Project)

Description: 
Handles the Computer Vision and AI inference using Google's MediaPipe.
This module serves as the software equivalent of the hardware posture_detector.

Responsibilities:
- Capture video frames from the CSI/USB camera.
- Process frames through the MediaPipe Pose model.
- Extract kinematic landmarks (specifically Head and Knees).
- Implement the mathematical logic to determine if a fall has occurred.
"""
