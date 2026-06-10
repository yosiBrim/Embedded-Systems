# Project Overview: Edge AI Fall Detection

## 1. System Architecture

* **Top-Level Controller (`main.py`):** Acts as the system FSM (Finite State Machine). It manages states, video acquisition via OpenCV, and implements temporal noise filtering (Debounce threshold of 2 consecutive frames with an 80% aspect ratio margin).
* **AI Processing Core (`pose_engine.py`):** Dedicated software IP Core utilizing OpenCV DNN and a pre-trained MobileNet-SSD model for lightweight, real-time object detection and bounding box extraction without overloading the CPU.
* **Hardware Interface (`i2c_display.py`):** Hardware Abstraction Layer (HAL) for the external 0.96" SSD1306 OLED display.

## 2. FPGA vs. Python Implementation Comparison

| Component (Python) | FPGA Equivalent (VHDL) | Engineering Role |
| :--- | :--- | :--- |
| `main.py` | `fall_detection_top.vhd` | Logic Control (FSM), Routing & Debounce Filter |
| `cv2.VideoCapture` | `OV7670_Controller.vhd` | Data Acquisition (Camera Interface) |
| `pose_engine.py` | `Deep_Learning_IP.vhd` | AI Object Detection & Feature Extraction |
| `i2c_display.py` | `I2C_OLED_Controller.vhd` | External Hardware Communication (I/O) |

## 3. Hardware Abstraction Layer (HAL)

* **`I2CDisplay` Class:** Manages I2C communication with the physical SSD1306 OLED screen (Operating at I2C address `0x3C`).
* **`show_message(message)`:** Unified function for message delivery. Includes fallback to terminal simulation (SIL mode) if hardware is disconnected.
* **`clear()`:** Display buffer clearing.

## 4. Completed Milestones

* **OS & Environment Configuration:** Enabled I2C and CSI interfaces via `raspi-config`. Successfully configured the local Python environment (resolving PEP 668 `externally-managed-environment` restrictions) to install required runtime dependencies (`opencv-python`, `luma.oled`).
* **OLED Hardware Integration:** Successfully mapped and connected the physical 0.96" OLED display. Validated I2C communication logic (Stuck Bus resolution) and successfully executed a hardware-level rendering test.

## 5. Next Engineering Steps (Roadmap & Troubleshooting)

* **Camera Hardware Debugging:** Resolve the V4L2 `select() timeout` and camera pipeline failures by performing a physical hardware inspection (re-seating the CSI ribbon cable orientation and pressing the internal "Sunny" sensor connector).
* **Video Stream Integration:** Extract a stable live frame from the physical camera using OpenCV (`cv2.VideoCapture`) and pipe it into the `PoseEngine`.
* **AI Logic Validation:** Verify the dynamic geometric inference logic (Bounding Box Aspect Ratio: `Width > Height * 0.8`) in a live physical environment.
