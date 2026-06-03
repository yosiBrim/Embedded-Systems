
"""
Module: i2c_display.py
Project: Edge AI Fall Detection System (Software PoC)
Description: Hardware Abstraction Layer (HAL) for the JMD0.96C OLED display (SSD1306).
Includes fallback to terminal simulation if hardware is not detected.
"""

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas

class I2CDisplay:
    """Manages the physical OLED screen via I2C."""

    def __init__(self):
        """Initializes the I2C bus and the SSD1306 OLED device."""
        print("I2CDisplay: Initializing hardware...")
        self.is_connected = False
        self.device = None
        
        try:
            # Default I2C address for these screens is usually 0x3C
            self.serial = i2c(port=1, address=0x3C)
            self.device = ssd1306(self.serial)
            self.is_connected = True
            print("I2CDisplay: OLED connected successfully.")
        except Exception as e:
            print(f"I2CDisplay WARNING: Hardware init failed ({e}).")
            print("Falling back to terminal simulation mode.")

    def show_message(self, message):
        """
        Displays a string on the OLED screen.
        If the screen is unavailable, prints to the terminal.
        """
        if self.is_connected:
            # The canvas object handles the display buffer
            with canvas(self.device) as draw:
                # Draw a black rectangle to clear the previous frame
                draw.rectangle(self.device.bounding_box, outline="black", fill="black")
                # Write the text at coordinates (x=10, y=25)
                draw.text((10, 25), message, fill="white")
        else:
            # Simulation fallback
            print(f"[DISPLAY OUT]: {message}")

    def clear(self):
        """Clears the screen buffer completely."""
        if self.is_connected:
            self.device.clear()
        else:
            print("[DISPLAY OUT]: --- SCREEN CLEARED ---")
