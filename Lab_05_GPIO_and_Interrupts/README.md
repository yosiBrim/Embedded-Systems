# Lab 5: GPIO Interfacing and Logic Control ⚡

## Overview
This laboratory explores direct hardware interaction using the Raspberry Pi General Purpose Input/Output (GPIO) pins. The focus is on bridging software logic with physical electrical components, moving from basic continuous polling to efficient, event-driven hardware control.

## 🛠️ Technical Key Highlights

### 1. Hardware Topologies (Active High/Low)
* Designed and tested circuits demonstrating both Active High and Active Low configurations.
* Controlled output states dynamically via Python using the `RPi.GPIO` library.

### 2. Internal Pull-Up/Pull-Down Configuration
* Eliminated the need for external resistors for button inputs by configuring the SoC's internal Pull-Up (`PUD_UP`) resistors via software.
* Demonstrated state transitions triggered by connecting the GPIO pin to the common ground.

### 3. Asynchronous Interrupt Handling
* Upgraded from blocking polling loops to **Hardware Interrupts**.
* Utilized edge detection (`GPIO.FALLING`) and callback functions to trigger events (e.g., doubling LED blink frequency) instantaneously.
* Implemented software debouncing (`bouncetime`) to prevent noisy mechanical switch signals from causing multiple rapid triggers.

### 4. 7-Segment State Machine
* Developed a digital counter mapping numerals (0-9) to a 7-segment display via a custom dictionary logic structure.
* Integrated an interrupt-driven direction toggle (counting Up/Down) without interrupting the main timing loop.

---

## 📝 Deliverables
* **Python Scripts:** `part_a.py`, `part_b.py`, `part_c.py`
* **Full Technical Report & Wokwi Schematics:** [Lab_5_GPIO_Interfacing_and_Logic_Control.pdf](./Lab_5_GPIO_Interfacing_and_Logic_Control.pdf)
