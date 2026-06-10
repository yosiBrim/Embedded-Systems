# Setup & Execution Guide: Edge AI Fall Detection

This guide provides step-by-step instructions for configuring the hardware and software environment to run the Edge AI Fall Detection PoC on a Raspberry Pi.

## 🛠️ 1. Hardware Assembly

Before powering on the Raspberry Pi, ensure all physical connections are secure.

### Camera Module
* Connect the **Raspberry Pi Camera Module 3** to the **CSI port** (located between the HDMI and Audio ports).
* Ensure the silver contacts on the ribbon cable face the HDMI port.
* **Important:** Gently press the small "Sunny" connector on the camera board itself to ensure it hasn't loosened, preventing `select() timeout` errors.

### OLED Display (I2C)
Connect the 0.96" SSD1306 OLED display to the Raspberry Pi GPIO header:

| OLED Pin | RPi GPIO Pin | Description |
| :--- | :--- | :--- |
| **VCC** | Pin 1 (3.3V) | Power supply |
| **GND** | Pin 6 (GND) | Ground |
| **SCL** | Pin 5 (GPIO 3) | I2C Clock |
| **SDA** | Pin 3 (GPIO 2) | I2C Data |

---

## ⚙️ 2. OS & Interface Configuration

Boot up the Raspberry Pi and open a terminal.

1. **Open the Raspberry Pi Configuration Tool:**
   ```bash
   sudo raspi-config
   ```
2. **Enable I2C:**
   * Navigate to `3 Interface Options` -> `I4 I2C`.
   * Select `Yes` to enable the ARM I2C interface.
3. **Enable Camera (Legacy/Libcamera):**
   * Depending on your OS version, navigate to `Interface Options` and ensure the Camera/Legacy Camera is enabled. (Note: This project uses `Picamera2` which relies on the modern `libcamera` stack).
4. **Reboot the system:**
   ```bash
   sudo reboot
   ```

**Verify Hardware:**
Run the following command to detect the OLED display on the I2C bus:
```bash
i2cdetect -y 1
```
*You should see the address `3c` populated in the grid.*

---

## 🐍 3. Software Environment & Dependencies

To avoid Python's PEP 668 `externally-managed-environment` restriction on modern Raspberry Pi OS, we will use a virtual environment.

1. **Update system packages and install system requirements:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y python3-venv i2c-tools libcamera-dev python3-opencv
   ```

2. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[YOUR-USERNAME]/Final_Project_Edge_AI_Fall_Detection.git
   cd Final_Project_Edge_AI_Fall_Detection
   ```

3. **Create and activate a Python virtual environment:**
   ```bash
   python3 -m venv .venv --system-site-packages
   source .venv/bin/activate
   ```
   *(Note: The `--system-site-packages` flag is crucial for inheriting the natively compiled `Picamera2` and `cv2` OS packages).*

4. **Install required Python libraries:**
   ```bash
   pip install luma.oled numpy
   ```

---

## 🚀 4. Running the System

With the hardware connected and the environment active, execute the top-level script:

```bash
python3 main.py
```

### Expected Behavior:
1. The OLED display will initialize and show `Status: Normal`.
2. The `Picamera2` sensor will warm up and stream frames directly to the AI engine.
3. The terminal will output live bounding box dimensions (`W` and `H`).
4. If a person drops to the floor (or mimics a fall where $Width > Height \times 0.8$ for 2 consecutive frames), the terminal will report a state transition, and the OLED will flash **`ALERT: FALL!`**.

### Stopping the System Safely
To terminate the program, press:
**`Ctrl + C`**
The system implements a Graceful Shutdown routine that safely stops the camera pipeline and clears the I2C OLED buffer before exiting.
