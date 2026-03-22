from machine import Pin, PWM
import time

led_pwm = PWM(Pin(15))
led_pwm.freq(5000)

print("--- Triangular Wave Generator ---")

try:
    freq = float(input("Enter frequency (Hz) [1-2 recommended]: "))
    amp = int(input("Enter amplitude (0-1023): "))
    
    if amp > 1023: amp = 1023
    if amp <= 0: amp = 1
    if freq <= 0: freq = 1
    
    step_delay = 1.0 / (2 * amp * freq)
    print(f"Starting! Freq: {freq}Hz, Max Amplitude: {amp}")
    
    while True:
        # שלב העלייה
        for duty in range(0, amp + 1):
            led_pwm.duty(duty)
            time.sleep(step_delay)
            
        # שלב הירידה
        for duty in range(amp - 1, -1, -1):
            led_pwm.duty(duty)
            time.sleep(step_delay)

except ValueError:
    print("Please enter numeric values only.")
