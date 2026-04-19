from machine import Pin, PWM, ADC
import time

# ADC Configuration (Potentiometer on GPIO 34)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB) 

# PWM Configuration (Servo on GPIO 15, 50Hz)
servo = PWM(Pin(15), freq=50)

def map_value(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

print("--- Task 1: Servo Motor Control Started ---")

while True:
    val = pot.read() # Reading ADC (0-4095)
    duty = map_value(val, 0, 4095, 40, 115) # Mapping to Servo Duty Cycle
    servo.duty(duty)
    print(f"Pot Value: {val} | Servo Duty: {duty}")
    time.sleep(0.05)
