# Project Overview: Edge AI Fall Detection

## 1. System Architecture
- **Top-Level Controller (`main.py`):** Acts as the system FSM (Finite State Machine), managing states: `INIT`, `MONITOR`, and `FALL_DETECTED`.
- **AI Processing Core (`pose_engine.py`):** Dedicated module for pose estimation analysis.
- **Hardware Interface (`i2c_display.py`):** Hardware Abstraction Layer (HAL) for the I2C display.

## 2. FPGA vs. Python Implementation Comparison
| Component (Python) | FPGA Equivalent | Engineering Role |
| :--- | :--- | :--- |
| **`main.py`** | **Top-Level Entity** | Logic Control (FSM) & Connectivity |
| **`pose_engine.py`** | **IP Core** | Data Processing (AI Pipeline) |
| **`i2c_display.py`** | **I/O Controller** | External Communication (I2C) |
| **`while True` Loop** | **System Clock / Logic** | Sampling & Synchronization |

## 3. Hardware Abstraction Layer (HAL)
- **`I2CDisplay` Class:** Manages communication with the external LCD/OLED display.
    - `show_message(message)`: Unified function for message delivery.
    - `clear()`: Display buffer clearing.

## 4. Next Engineering Steps (Roadmap)
1. **Camera Driver Setup:** Initialize the OV7670 camera and configure registers via I2C.
2. **Video Stream Processing:** Integrate the raw buffer from the camera into the `PoseEngine`.
3. **Performance Optimization:** Ensure FPS is sufficient for real-time detection on the Artix-7/Raspberry Pi pipeline.
4. **Final System Testing:** Validation in a controlled environment.
