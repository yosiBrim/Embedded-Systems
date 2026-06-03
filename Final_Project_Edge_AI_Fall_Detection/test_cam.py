import cv2
import time

# פתיחת המצלמה
cap = cv2.VideoCapture(0)

# הכרחת רזולוציה שפויה שמתאימה ל-Edge AI ומונעת קריסת זיכרון
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Camera opened successfully at 640x480! Press 'q' to quit.")

# נותנים למצלמה שנייה לכייל את הפוקוס
time.sleep(1)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Warning: Missed a frame, skipping...")
        time.sleep(0.1)
        continue
    
    cv2.imshow("Raspberry Pi Camera Test", frame)
    
    # המתנה ללחיצה על 'q' (זכור להקליק קודם על החלון!)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
