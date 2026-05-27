# Edge AI Fall Detection System: Hardware vs. Software PoC

## 📌 Project Overview
This project is a Proof of Concept (PoC) for an Edge Computing based fall-detection system, developed as a mini-project for the **Embedded Electronic Systems (130344)** course. 

It serves as a software-centric comparative counterpart to our primary senior design project, which implements the same logic utilizing custom RTL, BRAM, and bare-metal SCCB/VGA controllers on an Artix-7 FPGA. Here, we evaluate the development agility and performance of utilizing a microcomputer running an OS with pre-trained AI models.

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
* `i2c_display.py`: Hardware communication driver for the screen.
* `docs/`: Contains project proposal, draw.io diagrams, and the IEEE paper draft.

## 🔌 Hardware Pinout & Connections
| Component | RPi 3 Interface | Notes |
| :--- | :--- | :--- |
| Camera Module 3 | CSI Port | Located between HDMI and Audio Jack. |
| I2C Display (Pending) | GPIO 2 (SDA), GPIO 3 (SCL) | Requires 3.3V/5V VCC and GND. |

## 🚀 Development Roadmap (Milestones)
- [x] **Phase 0:** Project initialization, GitHub repository, and LaTeX skeleton.
- [ ] **Phase 1:** Physical camera setup and interface configuration.
- [ ] **Phase 2:** Implement `pose_engine.py` (AI integration).
- [ ] **Phase 3:** Main loop integration and terminal-based logic testing.
- [ ] **Phase 4:** I2C Display integration (`i2c_display.py`).
- [ ] **Phase 5:** Final testing and IEEE documentation.
