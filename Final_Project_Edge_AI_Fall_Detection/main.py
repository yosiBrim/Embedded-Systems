import cv2
import time
from pose_engine import PoseEngine
from i2c_display import I2CDisplay

class FallDetectionSystem:
    def __init__(self, video_source='fall_sample.mp4'):
        self.engine = PoseEngine()
        self.display = I2CDisplay()
        self.video_source = video_source
        print("System Initialized. Running in SIL mode.")

    def run(self):
        cap = cv2.VideoCapture(self.video_source)
        fall_frames_count = 0
        fall_detected_state = False

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            geometry = self.engine.process_frame(frame)
            current_frame_fall = False

            if geometry:
                # שורת הדיבוג שתראה לנו את המספרים בלייב
                print(f"Debug -> W: {geometry['w']}, H: {geometry['h']}")

                if geometry['w'] > (geometry['h'] * 0.8):
                    fall_frames_count += 1
                else:
                    fall_frames_count = 0

                # רגישות מוגברת: מספיקים 2 פריימים כדי לזהות נפילה
                if fall_frames_count >= 2:
                    current_frame_fall = True

            if current_frame_fall and not fall_detected_state:
                fall_detected_state = True
                self.display.show_message("ALERT: FALL!")
                print("FSM State Transition: [NORMAL] -> [FALL DETECTED]")
            elif not current_frame_fall and fall_detected_state:
                fall_detected_state = False
                self.display.show_message("Status: Normal")
                print("FSM State Transition: [FALL DETECTED] -> [NORMAL]")

            cv2.imshow("Edge AI Simulator", frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    system = FallDetectionSystem()
    system.run()
