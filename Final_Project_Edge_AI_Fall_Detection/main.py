import cv2
import time
from picamera2 import Picamera2
from pose_engine import PoseEngine
from i2c_display import I2CDisplay

class FallDetectionSystem:
    def __init__(self):
        self.engine = PoseEngine()
        self.display = I2CDisplay()
        
        # אתחול צינור הנתונים הישיר לחומרת המצלמה
        print("Initializing Hardware Camera (Picamera2)...")
        self.picam2 = Picamera2()
        config = self.picam2.create_video_configuration(main={"size": (640, 480)})
        self.picam2.configure(config)
        
        print("System Initialized. Running in LIVE Edge Hardware mode.")

    def run(self):
        self.picam2.start()
        print("Warming up sensor...")
        time.sleep(2)  # זמן לייצוב חשיפה לאור
        
        self.display.show_message("Status: Normal")
        
        fall_frames_count = 0
        fall_detected_state = False

        print("Starting live FSM inference loop. Press Ctrl+C to stop.")
        
        try:
            while True:
                # 1. דגימת פריים ישירות מהחומרה והמרה לפורמט OpenCV
                frame = self.picam2.capture_array()
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                # 2. חילוץ מאפיינים וגיאומטריה דרך מנוע ה-AI
                geometry = self.engine.process_frame(frame_bgr)
                current_frame_fall = False

                if geometry:
                    # שורת הדיבוג שתראה לנו את המספרים בלייב בטרמינל
                    print(f"Debug -> W: {geometry['w']}, H: {geometry['h']}")

                    if geometry['w'] > (geometry['h'] * 0.8):
                        fall_frames_count += 1
                    else:
                        fall_frames_count = 0

                    # 3. מנגנון Debounce: מספיקים 2 פריימים רצופים כדי לאמת
                    if fall_frames_count >= 2:
                        current_frame_fall = True
                else:
                    # אם לא זוהה אדם בפריים, מאפסים את המונה
                    fall_frames_count = 0

                # 4. מעברי FSM (מכונת מצבים) ופלט למסך ה-OLED
                if current_frame_fall and not fall_detected_state:
                    fall_detected_state = True
                    self.display.show_message("ALERT: FALL!")
                    print("FSM State Transition: [NORMAL] -> [FALL DETECTED]")
                
                elif not current_frame_fall and fall_detected_state:
                    fall_detected_state = False
                    self.display.show_message("Status: Normal")
                    print("FSM State Transition: [FALL DETECTED] -> [NORMAL]")

        except KeyboardInterrupt:
            # תפיסת לחיצת Ctrl+C לסגירה הנדסית בטוחה
            print("\nGraceful shutdown requested...")
        finally:
            self.picam2.stop()
            self.display.clear()
            print("System Offline. Hardware released.")

if __name__ == "__main__":
    system = FallDetectionSystem()
    system.run()
