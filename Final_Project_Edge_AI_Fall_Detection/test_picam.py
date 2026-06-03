import cv2
from picamera2 import Picamera2

print("Initializing camera...")

# אתחול המצלמה בדרך החדשה והרשמית
picam2 = Picamera2()

# הגדרת רזולוציה שפויה שמתאימה ל-Edge AI ול-Remote Desktop
config = picam2.create_video_configuration(main={"size": (640, 480)})
picam2.configure(config)

# הדלקת המצלמה
picam2.start()
print("Camera running flawlessly! Press 'q' to quit.")

while True:
    try:
        # משיכת התמונה ישירות מהחומרה כמערך שמוכן ל-OpenCV
        frame = picam2.capture_array()
        
        # הצגת החלון
        cv2.imshow("Raspberry Pi Camera Test", frame)
        
        # המתנה ללחיצה על 'q' (זכור להקליק על החלון של הווידאו קודם!)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print(f"Error: {e}")
        break

# סגירה מסודרת
picam2.stop()
cv2.destroyAllWindows()
