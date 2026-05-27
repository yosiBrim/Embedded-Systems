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
* `main.py`: The central execution loop (Software equivalent to the FPGA Top-Level). Includes camera initialization and temporal noise filtering (Debounce).
* `pose_engine.py`: AI inference and mathematical logic (Software equivalent to the `posture_detector` block).
* `i2c_display.py`: Hardware abstraction layer (HAL) for the screen.
* `requirements.txt`: Python package dependencies.
* `docs/`: Contains project proposal, draw.io diagrams, and the IEEE paper draft.

## 🔌 Hardware Pinout & Connections
| Component | RPi 3 Interface | Notes |
| :--- | :--- | :--- |
| Camera Module 3 | CSI Port | Located between HDMI and Audio Jack. |
| I2C Display | GPIO 2 (SDA), GPIO 3 (SCL) | Requires 3.3V/5V VCC and GND. |

## 💡 Key Engineering Insights (FPGA vs. Software PoC)
1. **Resource Management:** Instead of writing RTL modules for spatial downsampling and BRAM management (as in FPGA), the PoC leverages MediaPipe's `model_complexity=0` to abstract image scaling and optimize CPU load.
2. **Noise Filtering (Debounce):** The VHDL FSM uses a clock-cycle counter to prevent false positives from glitchy frames. In our Python implementation, this logic is identically replicated in `main.py` using a frame-counter threshold (`consecutive_falls >= 3`), achieving the same hysteresis effect in software.

## 🚀 Development Roadmap (Milestones)
- [x] **Phase 0:** Project initialization, GitHub repository, and LaTeX skeleton.
- [x] **Phase 1:** Software architecture, basic FSM logic, and HAL implementation.
- [x] **Phase 2:** AI Software Integration (MediaPipe geometric modeling) and Top-Level Debounce implementation.
- [ ] **Phase 3:** Hardware Setup: Enable OS CSI port, install dependencies (`requirements.txt`), and physical camera test.
- [ ] **Phase 4:** Live Validation: Run physical video stream through `main.py` to evaluate real-time FPS and confidence scores.
- [ ] **Phase 5:** Hardware Output: Physical I2C Display wiring and logic integration.
- [ ] **Phase 6:** Final system validation and IEEE documentation update.
