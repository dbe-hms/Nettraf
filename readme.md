# 🧩 NetworkSim  

> Tools and scripts for simulating real-world network conditions such as packet loss, delay, jitter, and disconnections.

This project is designed to run on a **Raspberry Pi** equipped with **two network adapters**.  
By bridging the adapters, you can introduce various network faults and performance degradations to test the robustness of networked systems.

---

## ✨ Features  

- Create and remove a network bridge between two interfaces  
- Simulate network conditions such as:  
  - Packet loss  
  - Latency and jitter  
  - Bandwidth throttling  
  - Temporary disconnections  
- Run interactively or automatically at startup  

---

## ⚙️ Requirements  

### Software  

```bash
sudo apt update
sudo apt install -y bridge-utils python3
```

### Hardware  

- Raspberry Pi (tested on Pi 4)  
- Secondary Ethernet interface (e.g., USB-to-Ethernet adapter)  

---

## 🚀 Getting Started  

### 1. Clone the repository  

```bash
git clone https://github.com/<your-username>/NetworkSim.git
cd NetworkSim
```

### 2. Setup the bridge  

Create a bridge between **eth0** and **eth1**:  
```bash
./setup_bridge.sh
```

Remove the bridge when done:  
```bash
./remove_bridge.sh
```

---

## 🧪 Simulation Scripts  

- **`cycle_issues.py`** — Cycles through random network conditions (delay, packet loss, disconnection, etc.)  
- **`Uinput_issues.py`** — Interactive mode allowing you to select network conditions manually via terminal  

---

## 🔁 Auto-Start at Boot  

To automatically set up the bridge and begin simulation at startup:  

1. Open the root crontab editor:  
   ```bash
   sudo crontab -e
   ```

2. Add the following lines to the bottom (update the paths as needed):  
   ```bash
   @reboot /home/pi/NetworkSim/setup_bridge.sh >> /home/pi/NetworkSim/log.log 2>&1
   @reboot /usr/bin/python3 /home/pi/NetworkSim/cycle_issues.py >> /home/pi/NetworkSim/log.log 2>&1
   ```

---

## 🧰 Notes  

- Always test carefully — these scripts intentionally disrupt network traffic.  Using SSH via an effected port may cause issues.   
- Logs will be written to `log.log` if configured in cron.  
- You can stop the simulation by removing the bridge or killing the Python process.

---

## 🧑‍💻 Author  

Deryck

