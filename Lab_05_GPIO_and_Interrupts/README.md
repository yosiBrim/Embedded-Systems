# Lab 5: GPIO Interfacing and Logic Control 🚦

## 📌 Overview
[cite_start]This laboratory focuses on General Purpose Input/Output (GPIO) operations within an Embedded Linux environment[cite: 96]. [cite_start]The transition from software logic to physical hardware interaction is demonstrated through LED actuation, button input sensing, and the implementation of a 7-Segment digital counter via serial communication[cite: 97].

## 🛠️ Tasks Performed

### 1. Frequency-Controlled LED (Active High/Low)
* [cite_start]Toggled an LED on GPIO 11 at a constant 1Hz frequency[cite: 105].
* [cite_start]Explored Active High and Active Low circuit topologies, validating that hardware polarity can be seamlessly managed and abstracted via software logic[cite: 106, 226].

### 2. Interrupt-Driven Input and Frequency Scaling
* [cite_start]Interfaced a push-button on GPIO 15, utilizing the SoC's internal Pull-Up resistor (`GPIO.PUD_UP`) to optimize hardware resources[cite: 149, 167, 227].
* [cite_start]Implemented asynchronous hardware interrupts (edge detection on `GPIO.FALLING`) to dynamically double the LED blink frequency[cite: 149, 151, 168]. [cite_start]This event-driven approach ensures the CPU is not monopolized by polling, meeting real-time responsiveness requirements[cite: 230, 231].

### 3. Synchronous Serial Communication (I2C)
* [cite_start]Established an I2C communication protocol using the Python `smbus2` library[cite: 172].
* [cite_start]Acted as the bus master to format and transmit a 4-digit integer sequence to an external Serial 7-Segment display module (address `0x71`)[cite: 174, 182].

## 💡 Key Engineering Insights
* [cite_start]**Hardware Abstraction:** Software logic can manage physical polarity, allowing for greater flexibility in component selection and PCB design[cite: 226].
* [cite_start]**Resource Optimization:** Leveraging internal pull-up/pull-down resistors simplifies external schematics and minimizes hardware failure points[cite: 227, 228].
* [cite_start]**Event-Driven Architecture:** Replacing blocking `while` loops with edge-triggered callbacks is fundamental for efficient Embedded Linux system design[cite: 229, 230, 231].

[cite_start]*Note: To ensure maximum clarity, all circuit diagrams in this documentation were generated using the Wokwi simulation environment, providing a standardized and highly readable schematic layout[cite: 99, 100].*
