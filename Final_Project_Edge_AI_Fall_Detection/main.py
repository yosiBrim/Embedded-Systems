"""
Module: main.py
Project: Edge AI Fall Detection System (Software PoC)
Description: Top-level system controller. Manages video acquisition, 
integrates AI processing, implements FSM with hysteresis (debounce), 
and triggers hardware outputs.
"""

import time
import cv2
from pose_engine import PoseEngine
from i2c_display import I2CDisplay

class FallDetectionSystem:
    """Main controller integrating Camera, AI Core, and Hardware Display."""

    def __init__(self):
        """Initializes system modules and FSM parameters."""
        print("System Initialization Started...")
        self.engine = PoseEngine()
        self.display = I2CDisplay()
        
        # FSM Debounce Parameters (Hysteresis)
        self.fall_threshold_frames = 3  # צריכים 3 פריימים רצופים של נפילה כדי להזעיק
        self.consecutive_falls = 0
        
        print("System Initialized Successfully.")

    def run(self):
        """Executes the main monitoring loop (Acquisition -> AI -> Output)."""
        # פתיחת מצלמת ה-CSI (0 מייצג את המצלמה הראשית)
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("ERROR: Cannot open camera.")
            return

        print("Starting video stream. Press 'q' to quit.")

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Warning: Dropped frame.")
                    continue
                
                # 1. AI Processing
                is_fall, confidence = self.engine.process_frame(frame)
                
                # 2. FSM Logic (Debounce / Noise filtering)
                if is_fall:
                    self.consecutive_falls += 1
                else:
                    self.consecutive_falls = 0 # איפוס אם האדם קם
                
                # 3. Hardware Output & State Evaluation
                if self.consecutive_falls >= self.fall_threshold_frames:
                    # הוספנו %.2f כדי להציג את האחוזים בשתי ספרות אחרי הנקודה
                    self.display.show_message(f"ALERT: FALL! (Conf: {confidence:.2f})")
                else:
                    self.display.show_message("Status: Normal")
                
                # (Optional Debugging): הצגת הוידאו על המסך (אם יש מסך מחובר לפאי)
                cv2.imshow('Fall Detection PoC - Debug View', frame)
                
                # יציאה מסודרת בלחיצה על 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        finally:
            # Clean shutdown (חשוב מאוד ב-Embedded)
            cap.release()
            cv2.destroyAllWindows()
            self.display.clear()
            print("System Shutdown Complete.")

if __name__ == "__main__":
    system = FallDetectionSystem()
    system.run()
