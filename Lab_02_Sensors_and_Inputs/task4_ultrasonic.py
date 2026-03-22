from machine import Pin, time_pulse_us
import time

# פינים לחיישן המרחק
trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

# פינים לנורת ה-RGB
red_led = Pin(12, Pin.OUT)
green_led = Pin(13, Pin.OUT)
blue_led = Pin(14, Pin.OUT)

def get_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    duration = time_pulse_us(echo, 1, 30000)
    
    if duration < 0:
        return -1
        
    distance = (duration * 0.0343) / 2
    return distance

def turn_off_all():
    red_led.value(0)
    green_led.value(0)
    blue_led.value(0)

print("--- Reverse Parking System Active ---")

while True:
    dist = get_distance()
    
    if dist < 0:
        print("No obstacle detected.")
        turn_off_all()
    else:
        print(f"Distance: {dist:.1f} cm")
        turn_off_all()
        
        # לוגיקת הצבעים לפי המרחק
        if dist > 20:
            green_led.value(1)
        elif 10 <= dist <= 20:
            blue_led.value(1)
        elif dist < 10:
            red_led.value(1)
            
    time.sleep(0.5)
