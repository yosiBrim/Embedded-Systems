# Lab 2: Sensors, Inputs, and PWM Signal Generation

This folder contains the documentation and source code for the second laboratory in the Embedded Electronic Systems course. The project focuses on integrating analog and digital sensors with an ESP32 microcontroller using MicroPython.

## 🛠️ Tasks & Hardware Implementations

The lab is divided into four distinct standalone scripts:

1. **`task1_rgb_pwm.py`:** Controls an RGB LED by mapping user-input color values (0-255) to precise PWM duty cycles.
2. **`task2_ldr.py`:** An Automatic Lighting System that uses a Light Dependent Resistor (LDR) connected to the ESP32's ADC to inversely control an LED's brightness based on ambient light.
3. **`task3_triangle_wave.py`:** A signal generator that creates a triangular wave via PWM, resulting in a smooth "breathing" effect on an LED.
4. **`task4_ultrasonic.py`:** A Reverse Parking Sensor simulation using an HC-SR04 ultrasonic distance sensor. It calculates pulse duration to determine distance and triggers conditional color changes on an RGB LED.

## 📄 Documentation
The complete methodology, expected theoretical outcomes, Wokwi simulation proofs, and circuit designs can be found in the attached `lab_2_ambedded.pdf` report.
