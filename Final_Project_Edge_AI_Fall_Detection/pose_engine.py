"""
Module: pose_engine.py
Project: Edge AI Fall Detection System (Software PoC)

================================================================================
MACRO-LEVEL (System Architecture Role):
This module serves as the "AI IP Core" for our Edge Computing Proof of Concept. 
In the broader context of the project, it acts as the software equivalent of the 
custom Posture Detection RTL block designed for the Artix-7 FPGA. 
By isolating the AI inference from the main FSM and I/O controllers, it ensures 
modularity. It receives raw data (frames) from the Top-Level and returns purely 
processed states (fall detection flags), keeping the system architecture clean.

MICRO-LEVEL (Algorithmic Operation):
This module instantiates Google's lightweight MediaPipe Pose estimation model.
Optimized for the Raspberry Pi 3 (model_complexity=0), it avoids heavy hardware 
utilization. The detection logic is deterministic and geometric:
1. Extracts spatial landmarks from the video frame.
2. Isolates the Y-coordinates of the Nose and Knees.
3. Applies a threshold equation: If (Y_nose > Y_average_knees) AND visibility 
   confidence is high -> A fall event is triggered.
================================================================================
"""

import cv2
import mediapipe as mp

class PoseEngine:
    """Encapsulates the MediaPipe AI model and posture-geometry logic."""

    def __init__(self):
        """Initializes the lightweight MediaPipe Pose model for Edge processing."""
        print("PoseEngine: Loading MediaPipe Pose Model...")
        self.mp_pose = mp.solutions.pose
        
        # model_complexity=0 is CRITICAL for Raspberry Pi 3 to maintain good FPS
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=0, 
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.confidence_threshold = 0.6

    def process_frame(self, frame):
        """
        Analyzes a single video frame to detect falls based on skeletal geometry.
        
        Args:
            frame: The raw image matrix (BGR format from OpenCV camera capture).
            
        Returns:
            tuple: (is_fall_detected (bool), confidence_score (float))
        """
        # Convert BGR (OpenCV standard format) to RGB (MediaPipe requirement)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Run AI inference to extract skeletal nodes
        results = self.pose.process(rgb_frame)
        
        is_fall = False
        confidence = 0.0
        
        # Proceed only if a human subject is detected in the frame
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            
            # Extract Y coordinates (Note: 0.0 is the top of the image, 1.0 is the bottom)
            nose_y = landmarks[self.mp_pose.PoseLandmark.NOSE.value].y
            left_knee_y = landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value].y
            right_knee_y = landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value].y
            
            # Calculate the mid-point of the knees
            avg_knee_y = (left_knee_y + right_knee_y) / 2.0
            
            # Extract visibility metrics to prevent false positives from hidden limbs
            nose_vis = landmarks[self.mp_pose.PoseLandmark.NOSE.value].visibility
            knee_vis = (landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value].visibility + 
                        landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value].visibility) / 2.0
            
            # DETECTION LOGIC: If the nose drops below the knees, and visibility is valid
            if nose_y > avg_knee_y and nose_vis > 0.5 and knee_vis > 0.5:
                is_fall = True
                # Use the lowest visibility score of the key nodes as the detection confidence
                confidence = min(nose_vis, knee_vis) 
                
        return is_fall, confidence

    def draw_skeleton(self, frame, results):
        """
        Optional debugging tool: Overlays the detected skeleton onto the video frame.
        Useful for visual validation before connecting the physical I2C display.
        """
        mp_drawing = mp.solutions.drawing_utils
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        return frame
