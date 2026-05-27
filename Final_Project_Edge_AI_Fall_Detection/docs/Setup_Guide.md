# 🛠️ Environment Setup & Remote Connection Guide

This guide documents how to remotely connect to the Raspberry Pi for development and debugging.

## Remote Desktop Connection (Windows MSTSC)
Since the Raspberry Pi runs headlessly (without a physical monitor), we use Windows Remote Desktop to access its graphical interface. This is required to view the OpenCV video windows during AI inference testing.

### Prerequisites (Run once on Pi via SSH)
To allow the Pi to accept RDP connections, the `xrdp` server must be installed:
`sudo apt update`
`sudo apt install xrdp -y`

### Connection Steps
1. Open **Remote Desktop Connection** (MSTSC) on Windows.
2. Enter the Raspberry Pi's IP address and click **Connect**.
3. Accept the certificate warning if prompted.
4. In the `xrdp` login screen, ensure the session is set to **Xorg**.
5. Enter the credentials (default: `pi` / `pi`).
