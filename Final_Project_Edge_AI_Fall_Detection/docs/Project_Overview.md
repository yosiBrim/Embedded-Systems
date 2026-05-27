# Project Overview: Edge AI Fall Detection

## 1. System Architecture
- **Top-Level Controller (`main.py`):** Acts as the system FSM (Finite State Machine), managing states: `INIT`, `MONITOR`, and `FALL_DETECTED`.
- **AI Processing Core (`pose_engine.py`):** Dedicated module for pose estimation analysis (equivalent to a hardware processing pipeline).
- **Hardware Interface (`i2c_display.py`):** Driver for status output via I2C protocol.

## 2. FPGA vs. Python Implementation Comparison
הטבלה הבאה מציגה את ההקבלה בין הפרויקט הנוכחי לבין ארכיטקטורת FPGA סטנדרטית:

| רכיב ב-Python (מערכת נוכחית) | רכיב מקביל ב-FPGA (חומרה) | תפקיד הנדסי |
| :--- | :--- | :--- |
| **`main.py`** | **Top-Level Entity** | ניהול לוגיקת המערכת (FSM) וקישוריות |
| **`pose_engine.py`** | **IP Core / Logic Module** | עיבוד נתונים ייעודי (AI Pipeline) |
| **`i2c_display.py`** | **I/O Controller** | בקר תקשורת חיצוני (I2C/VGA) |
| **`while True` Loop** | **System Clock / Logic** | קצב דגימת המערכת וסנכרון |



## 3. Current Implementation Status
- **FSM Logic:** Verified transitions between `MONITOR` and `FALL_DETECTED` states.
- **Module Integration:** `main.py` successfully instances `PoseEngine` and manages state-based output.

## 4. Next Steps (Roadmap)
1. **I2C Display Integration:** Connecting the output logic to `i2c_display.py`.
2. **Camera Integration:** Replacing dummy FSM logic with real-time video feed from the OV7670.
3. **Verification:** Testing the full pipeline in real-world conditions.
