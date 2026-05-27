# Edge AI Fall Detection System: Hardware vs. Software PoC

## 📌 Project Overview
This project is a Proof of Concept (PoC) for an Edge Computing based fall-detection system, developed as a mini-project for the **Embedded Electronic Systems (130344)** course. 

It serves as a software-centric comparative counterpart to our primary senior design project, which implements the same logic utilizing custom RTL, BRAM, and bare-metal SCCB/VGA controllers on an Artix-7 FPGA. Here, we evaluate the development agility and performance of utilizing a microcomputer running an OS with pre-trained AI models.

## ⚖️ FPGA vs. Python Implementation Comparison
To ensure alignment with the Artix-7 VHDL project, the following architectural mapping is maintained:

| Component (Python) | FPGA Equivalent (VHDL) | Engineering Role |
| :--- | :--- | :--- |
| **`main.py`** | **`fall_detection_top.vhd`** | Logic Control (FSM) & Structural Routing |
| **`cv2.VideoCapture`** | **`OV7670_Controller.vhd`** | Data Acquisition (Camera Interface) |
| **`pose_engine.py`** | **AI / Posture IP Core** | Data Processing (Algorithm execution) |
| **`i2c_display.py`** | **`VGA_Controller.vhd`** | External Hardware Communication (I/O) |
| **`while True` Loop** | **System Clock / FSM logic**| Sampling & Synchronization |

## 🏗️ System Architecture
The system is designed with a top-down modular approach, separating hardware interfacing from the software logic.

* **Input (Hardware):** Raspberry Pi Camera Module 3 (CSI Interface).
* **Processing (Software):** Raspberry Pi 3 running a Python loop.
    * Computer Vision & AI: Google MediaPipe (Pose Estimation).
    * Detection Logic: Deductive geometric analysis of skeletal Y-coordinates ($Y_{nose} > Y_{knees}$).
* **Output (Hardware):** I2C-based Digital Display (OLED/LCD).

## 🗂️ Repository Structure
* `main.py`: The central execution loop (Software equivalent to the FPGA Top-Level).
* `pose_engine.py`: AI inference and mathematical logic (Software equivalent to the `posture_detector` block).
* `i2c_display.py`: Hardware abstraction layer (HAL) for the screen.
* `docs/`: Contains project proposal, draw.io diagrams, and the IEEE paper draft.

## 🔌 Hardware Pinout & Connections
| Component | RPi 3 Interface | Notes |
| :--- | :--- | :--- |
| Camera Module 3 | CSI Port | Located between HDMI and Audio Jack. |
| I2C Display | GPIO 2 (SDA), GPIO 3 (SCL) | Requires 3.3V/5V VCC and GND. |

## 🚀 Development Roadmap (Milestones)
- [x] **Phase 0:** Project initialization, GitHub repository, and LaTeX skeleton.
- [x] **Phase 1:** Software architecture, FSM logic formulation, and HAL implementation.
- [ ] **Phase 2:** Physical camera setup and interface configuration (Enable CSI in OS & install OpenCV).
- [ ] **Phase 3:** Integrate video stream into `pose_engine.py` (AI model deployment).
- [ ] **Phase 4:** Main loop integration and performance optimization (FPS considerations).
- [ ] **Phase 5:** I2C Display hardware integration (`i2c_display.py`).
- [ ] **Phase 6:** Final testing, validation, and IEEE documentation update.
