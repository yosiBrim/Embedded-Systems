"""
Module: main.py
Project: Edge AI Fall Detection System (JCT Mini-Project)

Description: 
The central execution engine of the Edge AI Fall Detection System. 
This script replaces the hardware top-level and FSM (Finite State Machine).

Responsibilities:
- Initialize the AI engine (pose_engine) and hardware interface (i2c_display).
- Manage the continuous main execution loop (while True).
- Route the detection results from the AI module to the hardware display.
- Handle graceful system shutdown and resource cleanup.
"""
