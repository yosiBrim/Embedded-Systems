from machine import Pin, PWM
import sys

# הגדרת פיני PWM
red_pin = PWM(Pin(12), freq=5000)
green_pin = PWM(Pin(13), freq=5000)
blue_pin = PWM(Pin(14), freq=5000)

def set_color(r, g, b):
    # המרה לטווח 0-1023
    red_pin.duty(r * 4)
    green_pin.duty(g * 4)
    blue_pin.duty(b * 4)

print("--- RGB LED Control System ---")

while True:
    try:
        val_r = int(input("Enter RED value (0-255): "))
        val_g = int(input("Enter GREEN value (0-255): "))
        val_b = int(input("Enter BLUE value (0-255): "))
        
        if 0 <= val_r <= 255 and 0 <= val_g <= 255 and 0 <= val_b <= 255:
            set_color(val_r, val_g, val_b)
            print(f"Color updated: R={val_r}, G={val_g}, B={val_b}")
        else:
            print("Error: Values must be between 0 and 255!")
            
    except ValueError:
        print("Error: Please enter integers only.")
