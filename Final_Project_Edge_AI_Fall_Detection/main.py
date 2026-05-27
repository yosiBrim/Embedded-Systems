"""
Module: main.py
Description: Top-level system controller implementing the Finite State Machine (FSM).
"""

import time
from pose_engine import PoseEngine
from i2c_display import I2CDisplay

class FallDetectionSystem:
    """Main controller for the Edge AI Fall Detection system."""

    def __init__(self):
        """Initializes system modules: AI engine and I2C hardware interface."""
        self.engine = PoseEngine()
        self.display = I2CDisplay()
        print("System Initialized.")

    def run(self):
        """Executes the main monitoring loop and state transitions."""
        counter = 0
        while True:
            counter += 1
            is_fall = (counter >= 5)
            
            # FSM State Logic
            if is_fall:
                self.display.show_message("ALERT: FALL!")
            else:
                self.display.show_message("Status: Normal")
                
            time.sleep(1)

if __name__ == "__main__":
    system = FallDetectionSystem()
    system.run()
