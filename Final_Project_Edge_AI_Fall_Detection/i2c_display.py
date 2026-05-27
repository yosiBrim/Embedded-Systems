"""
Module: i2c_display.py
Project: Edge AI Fall Detection System (JCT Mini-Project)

Description: 
Manages the hardware-level I2C communication with the external LCD/OLED display.

Responsibilities:
- Initialize the I2C bus on the Raspberry Pi.
- Send standard operating status messages (e.g., "Status: Normal").
- Send critical alert messages upon detection (e.g., "ALERT: FALL!").
- Handle timing and buffer requirements for the specific I2C controller.
"""
