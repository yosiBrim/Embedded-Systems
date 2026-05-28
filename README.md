# Embedded Electronic Systems (130344) - Coursework & Labs 🔌

Welcome to my repository dedicated to the **Embedded Electronic Systems** course. As a final-year Electronics Engineering student, I use this space to document my hands-on laboratory work, hardware interfacing projects, and microcontroller programming.

This repository highlights my practical experience in bridging software and hardware, progressing from bare-metal-like MicroPython scripting to Embedded Linux applications, utilizing various communication protocols (SPI, I2C, UART, WiFi, Bluetooth).

## 📂 Course Repository Structure

### [Lab 1: MicroPython Basics & Controller Architecture](./Lab_01_MicroPython_Basics)
* **Status:** ✅ Completed
* **Topics:** Introduction to embedded systems, IDE setup, digital and analog I/O using ESP32 and MicroPython. Includes full Wokwi simulation proofs.

### [Lab 2: Sensors, Inputs, and PWM Signal Generation](./Lab_02_Sensors_and_Inputs)
* **Status:** ✅ Completed
* **Topics:** Interfacing with basic analog and digital inputs (LDR, Ultrasonic HC-SR04) and controlling outputs (RGB LED) using PWM. Includes full Wokwi simulation proofs.

### [Lab 3: Motors Control and Interfacing](./Lab_03_Motors)
* **Status:** ✅ Completed
* **Topics:** Implementation of precision motor control using MicroPython. Key areas include Analog-to-PWM mapping for Servo motors and designing a non-blocking state machine for Stepper motor actuation via the A4988 driver and digital inputs.
  
### [Lab 4: Introduction to Embedded Linux](./Lab_04_Embedded_Linux)
* **Status:** ✅ Completed
* **Topics:** Linux filesystem hierarchy, access control (octal permissions), and process management (foreground/background execution). Includes hands-on CLI practice and process signals.

### [Lab 5: GPIO Interfacing and Logic Control](./Lab_05_GPIO_and_Logic_Control)
* **Status:** ✅ Completed
* [cite_start]**Topics:** Transitioning from software logic to physical hardware interaction in Embedded Linux[cite: 96, 97]. [cite_start]Covers Active High/Low topologies, internal Pull-Up/Down configuration, asynchronous event handling via hardware interrupts, and synchronous serial communication (I2C) using the `smbus2` library to drive a 4-digit 7-segment display[cite: 98, 172, 174].

### [🚀 Final Project: Edge AI Fall Detection System (Software vs. FPGA PoC)](./Edge_AI_Fall_Detection)
* **Status:** 🏃‍♂️ Active / In Progress
* **Description:** A Proof of Concept (PoC) Edge Computing system utilizing a Raspberry Pi and the MediaPipe CV framework to detect human falls in real-time. This software-centric pipeline serves as a comparative counterpart to a custom RTL/VHDL implementation on an Artix-7 FPGA. It features a geometric skeletal logic engine and an I2C-driven SSD1306 OLED hardware abstraction layer (HAL).

## 🛠️ Technologies & Tools
* **Hardware:** ESP32, Raspberry Pi 3, 0.96" OLED (SSD1306), RPi Camera Module 3
* **Programming Languages:** MicroPython, Python, Bash/C
* **Actuators & Sensors:** DC/Servo Motors, LDR, 7-Segment, Ultrasonic, Video Sensors
* **Protocols & Interfaces:** GPIO, PWM, CSI, I2C, SPI, UART, WiFi, Bluetooth
* **Environments & Libraries:** Wokwi Simulation, Linux OS, OpenCV, MediaPipe
