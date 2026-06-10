# Project Overview: Edge AI Fall Detection

## 1. System Architecture

* **Top-Level Controller (`main.py`):** Acts as the system FSM (Finite State Machine). It manages states, video acquisition via the native `Picamera2` pipeline, and implements temporal noise filtering (Debounce threshold of 2 consecutive frames with an 80% aspect ratio margin). It also includes a Graceful Shutdown mechanism to safely release hardware resources upon exit.
* **AI Processing Core (`pose_engine.py`):** Dedicated software IP Core utilizing OpenCV DNN and a pre-trained MobileNet-SSD model for lightweight, real-time object detection and bounding box extraction without overloading the CPU.
* **Hardware Interface (`i2c_display.py`):** Hardware Abstraction Layer (HAL) for the external 0.96" SSD1306 OLED display.

## 2. FPGA vs. Python Implementation Comparison

| Component (Python) | FPGA Equivalent (VHDL) | Engineering Role |
| :--- | :--- | :--- |
| `main.py` | `fall_detection_top.vhd` | Logic Control (FSM), Routing & Debounce Filter |
| `Picamera2` (Native) | `OV7670_Controller.vhd` | Data Acquisition (Direct Hardware Pipeline) |
| `pose_engine.py` | `Deep_Learning_IP.vhd` | AI Object Detection & Feature Extraction |
| `i2c_display.py` | `I2C_OLED_Controller.vhd` | External Hardware Communication (I/O) |

## 3. Hardware Abstraction Layer (HAL)

* **`I2CDisplay` Class:** Manages I2C communication with the physical SSD1306 OLED screen (Operating at I2C address `0x3C`).
* **`show_message(message)`:** Unified function for message delivery. Includes fallback to terminal simulation (SIL mode) if hardware is disconnected.
* **`clear()`:** Display buffer clearing.

## 4. Completed Milestones

* **OS & Environment Configuration:** Enabled I2C and CSI interfaces via `raspi-config`. Successfully configured the local Python environment (resolving PEP 668 restrictions) to install required runtime dependencies (`opencv-python`, `luma.oled`).
* **OLED Hardware Integration:** Successfully mapped and connected the physical 0.96" OLED display. Validated I2C communication logic and successfully executed hardware-level rendering tests.
* **Hardware Data Pipeline Resolution:** Diagnosed and resolved OS-level V4L2 `select() timeout` failures by bypassing legacy abstractions and implementing a direct hardware pipeline using `Picamera2`, ensuring zero-latency data streaming from the IMX708 sensor.
* **Live System Integration:** Successfully fused the hardware inputs/outputs with the AI processing core. Validated the dynamic geometric inference logic (Bounding Box Aspect Ratio: `Width > Height * 0.8`) and FSM state transitions in a live physical environment.

## 5. Next Engineering Steps (Finalization & Documentation)

* **Parameter Tuning:** Calibrate the bounding box aspect ratio threshold (currently 0.8) based on different distances and angles to optimize the detection accuracy and minimize false positives during standard human movement.
* **Documentation & Reporting:** Finalize the IEEE standard project report, detailing the comparative analysis between the software edge-computing implementation and the primary physical synthesis on the Artix-7 100T (Nexys A7) FPGA architecture.
