# Project Overview: Edge AI Fall Detection

## 1. System Architecture
- **Top-Level Controller (`main.py`):** Acts as the system FSM (Finite State Machine). It manages states, video acquisition via OpenCV, and implements temporal noise filtering (Debounce threshold of 3 consecutive frames).
- **AI Processing Core (`pose_engine.py`):** Dedicated software IP Core utilizing Google MediaPipe (`model_complexity=0`) for lightweight, real-time geometric pose estimation without overloading the CPU.
- **Hardware Interface (`i2c_display.py`):** Hardware Abstraction Layer (HAL) for the external 0.96" SSD1306 OLED display.

## 2. FPGA vs. Python Implementation Comparison
| Component (Python) | FPGA Equivalent (VHDL) | Engineering Role |
| :--- | :--- | :--- |
| **`main.py`** | **`fall_detection_top.vhd`** | Logic Control (FSM), Routing & Debounce Filter |
| **`cv2.VideoCapture`** | **`OV7670_Controller.vhd`** | Data Acquisition (Camera Interface) |
| **`pose_engine.py`** | **AI / Posture IP Core** | Data Processing & Image Scaling |
| **`i2c_display.py`** | **`VGA_Controller.vhd`** | External Hardware Communication (I/O) |

## 3. Hardware Abstraction Layer (HAL)
- **`I2CDisplay` Class:** Manages I2C communication with the physical SSD1306 OLED screen.
    - `show_message(message)`: Unified function for message delivery. Includes fallback to terminal simulation if hardware is disconnected.
    - `clear()`: Display buffer clearing.

## 4. Next Engineering Steps (Roadmap)
1. **OS Configuration:** Enable the CSI camera port via `raspi-config` and install system dependencies using `pip install -r requirements.txt`.
2. **Video Stream Integration:** Pull the first live frame using OpenCV and pass it to the `PoseEngine`.
3. **AI Logic Validation:** Verify the geometric logic ($Y_{nose} > Y_{knees}$) in a live physical environment.
4. **Hardware Integration:** Connect the physical OLED display (VCC, GND, SDA, SCL) and route the FSM status flags to the screen.
