# 🛠️ Environment Setup & Remote Connection Guide

This guide documents how to remotely connect to the Raspberry Pi for development and debugging.

## Remote Desktop Connection (Windows MSTSC)
Since the Raspberry Pi runs headlessly (without a physical monitor), we use Windows Remote Desktop to access its graphical interface. This is required to view the OpenCV video windows during AI inference testing.

### Prerequisites (Run once on Pi via SSH)
To allow the Pi to accept RDP connections, the `xrdp` server must be installed:
`sudo apt update`
`sudo apt install xrdp -y`

---

## 🔌 Connection Scenarios

### Scenario A: College Network (Router Connection)
*Use this when the Pi is connected to the college network and receives a standard IP (e.g., `10.1.4.194`).*

1. Open **Remote Desktop Connection** (MSTSC) on Windows.
2. Enter the Raspberry Pi's assigned IP address and click **Connect**.
3. Accept the certificate warning if prompted.
4. In the `xrdp` login screen, ensure the session is set to **Xorg**.
5. Enter the credentials (default: `pi` / `pi`).

### Scenario B: Direct Cable to Personal Computer (Home Setup)
*Use this when connecting the Pi directly to your PC via an Ethernet cable, without a router.*

**Step 1: Share PC Internet with the Pi (Windows ICS)**
1. Press `Win + R`, type `ncpa.cpl`, and press Enter to open Network Connections.
2. Right-click your active **Wi-Fi** connection -> **Properties** -> **Sharing** tab.
3. Check the box: `"Allow other network users to connect through this computer's Internet connection"`.
4. From the drop-down, select the **Ethernet** connection attached to the Pi, then click **OK**.

**Step 2: Find the Pi's assigned IP Address**
1. Open Windows CMD and connect via the Pi's default IPv6 address:
   `ssh pi@fe80::bb51:9f0f:7c9b:82d7%9`
   *(Type `yes` if asked, password is `pi`)*
2. Once inside the Pi's terminal, run: 
   `hostname -I`
3. Copy the standard IPv4 address it outputs (usually looks like `192.168.137.X`).

**Step 3: Connect via Remote Desktop**
1. Open **Remote Desktop Connection** (MSTSC) on Windows.
2. Enter the copied IP address (e.g., `192.168.137.90`) and click **Connect**.
3. In the `xrdp` login screen, ensure the session is set to **Xorg**.
4. Enter the credentials (`pi` / `pi`).
