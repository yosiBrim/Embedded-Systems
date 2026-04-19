from machine import Pin
import time

# Pin Definitions
dir_pin = Pin(12, Pin.OUT)
step_pin = Pin(14, Pin.OUT)
btn_dir = Pin(26, Pin.IN, Pin.PULL_UP)
btn_steps = Pin(27, Pin.IN, Pin.PULL_UP)

# State Variables
current_dir = 0
step_options = [0, 10, 20, 30]
idx = 0
last_move = time.ticks_ms()
last_btn_dir = 0
last_btn_steps = 0

def move_stepper(steps):
    for _ in range(steps):
        step_pin.value(1)
        time.sleep_us(1000)
        step_pin.value(0)
        time.sleep_us(1000)

print("--- Task 2: Stepper Motor System Active ---")

while True:
    now = time.ticks_ms()
    
    # Non-blocking Direction Button Handling
    if btn_dir.value() == 0 and time.ticks_diff(now, last_btn_dir) > 250:
        current_dir = not current_dir
        dir_pin.value(current_dir)
        print(f"Direction changed: {'CW' if current_dir == 0 else 'CCW'}")
        last_btn_dir = now

    # Non-blocking Step Selection Button Handling
    if btn_steps.value() == 0 and time.ticks_diff(now, last_btn_steps) > 250:
        idx = (idx + 1) % 4
        print(f"Steps selected: {step_options[idx]}")
        last_btn_steps = now

    # Timed Execution (Every 5 seconds)
    if time.ticks_diff(now, last_move) >= 5000:
        s = step_options[idx]
        if s > 0:
            print(f"Executing {s} steps...")
            move_stepper(s)
        last_move = time.ticks_ms()
