# Lab 1: MicroPython Basics with ESP32

This repository contains the source code and documentation for Lab 1 of the Embedded Electronic Systems course. The project demonstrates fundamental hardware control using an ESP32 microcontroller and MicroPython within the Wokwi simulation environment.

## Project Overview

The main script (`main.py`) provides a unified, menu-driven interface via the serial terminal to execute four distinct hardware control tasks:

* **Task 1:** Blinking a single LED a user-specified number of times using basic GPIO digital output.
* **Task 2:** Lighting up a specific number of LEDs (from an array of 4) based on user input.
* **Task 3:** Activating a specific discrete LED (Red, Green, or Blue) based on a text command.
* **Task 4:** Generating complex colors (e.g., Purple, Orange) on an RGB LED using Pulse Width Modulation (PWM).

## Hardware Components

* ESP32 Microcontroller
* 4x Standard LEDs (for array)
* 1x RGB LED
* Current-limiting resistors

## Documentation & Proof

The project was fully simulated and verified using Wokwi. The enclosed `esp32_project_1.pdf` report contains the complete source code, expected theoretical results, and visual screenshot proofs for each executed task.

## Authors

* **Yosi Brim**
* **Elad Asbag**
