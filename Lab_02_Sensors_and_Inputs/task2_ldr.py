from machine import Pin, PWM, ADC
import time

led = PWM(Pin(15), freq=5000)
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

print("--- Auto Lighting System ---")

while True:
    light_value = ldr.read()
    
    # חישוב עוצמת ההארה (מותאם לחומרת המודול בסימולטור)
    duty_cycle = int(light_value / 4)
    
    # הגנה מחריגת טווחים
    if duty_cycle < 0: duty_cycle = 0
    if duty_cycle > 1023: duty_cycle = 1023
    
    led.duty(duty_cycle)
    print(f"LDR Value: {light_value} | LED Duty: {duty_cycle}")
    time.sleep(0.1)
