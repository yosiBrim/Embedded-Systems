print("Hello, ESP32!")
import machine
import time

# --- הגדרת פינים (Setup) ---

# משימה 1: LED מהבהב
led_task1 = machine.Pin(2, machine.Pin.OUT)

# משימה 2: 4 נורות LED
leds_task2 = [machine.Pin(i, machine.Pin.OUT) for i in (12, 13, 14, 15)]

# משימה 3: נורות צבעוניות נפרדות
led_red = machine.Pin(16, machine.Pin.OUT)
led_green = machine.Pin(17, machine.Pin.OUT)
led_blue = machine.Pin(18, machine.Pin.OUT)

# משימה 4: נורת RGB (שימוש ב-PWM כדי לאפשר יצירת גוונים כמו כתום וסגול)
pwm_r = machine.PWM(machine.Pin(25), freq=1000)
pwm_g = machine.PWM(machine.Pin(26), freq=1000)
pwm_b = machine.PWM(machine.Pin(27), freq=1000)

def set_rgb_color(r, g, b):
    # ב-ESP32 ערכי ה-PWM נעים בין 0 ל-1023
    # הפונקציה ממירה ערכי RGB סטנדרטיים (0-255) לערכי PWM
    pwm_r.duty(int((r / 255) * 1023))
    pwm_g.duty(int((g / 255) * 1023))
    pwm_b.duty(int((b / 255) * 1023))

# --- פונקציות לכל משימה ---

def task1():
    try:
        num = int(input("הכנס מספר להבהוב ה-LED: "))
        for _ in range(num):
            led_task1.value(1)
            time.sleep(0.5)
            led_task1.value(0)
            time.sleep(0.5)
    except ValueError:
        print("שגיאה: יש להזין מספר שלם.")

def task2():
    try:
        num = int(input("הכנס מספר בין 1 ל-4: "))
        if 1 <= num <= 4:
            for i in range(4):
                # מדליק את הנורות עד למספר שנקלט, ומכבה את השאר
                leds_task2[i].value(1 if i < num else 0)
        else:
            print("המספר מחוץ לטווח!")
    except ValueError:
        print("שגיאה: יש להזין מספר שלם.")

def task3():
    color = input("הכנס צבע (אדום, ירוק, כחול): ").strip()
    
    # כיבוי כל הנורות לפני הדלקה מחדש
    led_red.value(0)
    led_green.value(0)
    led_blue.value(0)
    
    if color == "RED":
        led_red.value(1)
    elif color == "GREEN":
        led_green.value(1)
    elif color == "BLUE":
        led_blue.value(1)
    else:
        print("צבע לא מוכר.")

def task4():
    color = input("הכנס צבע (אדום, ירוק, כחול, סגול, כתום, צהוב, לבן): ").strip()
    
    # מילון המכיל את ערכי ה-RGB לכל צבע
    colors = {
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "PURPLE": (128, 0, 128),
        "ORANGE": (255, 165, 0),
        "YALLOW": (255, 255, 0),
        "WHITE": (255, 255, 255)
    }
    
    if color in colors:
        set_rgb_color(*colors[color])
    else:
        print("צבע לא מוכר.")
        set_rgb_color(0, 0, 0) # כיבוי במקרה של שגיאה

# --- לולאה ראשית ---

while True:
    print("\n--- תפריט משימות ---")
    print("1. הבהוב LED לפי מספר")
    print("2. הדלקת כמות לדים (1-4)")
    print("3. הדלקת LED נפרד לפי צבע")
    print("4. הדלקת RGB LED לפי צבע")
    print("5. יציאה")
    
    choice = input("בחר משימה (1-5): ")
    
    if choice == '1':
        task1()
    elif choice == '2':
        task2()
    elif choice == '3':
        task3()
    elif choice == '4':
        task4()
    elif choice == '5':
        print("סיום תכנית.")
        break
    else:
        print("בחירה לא חוקית, נסה שוב.")
