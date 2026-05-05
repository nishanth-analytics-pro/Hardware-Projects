
# 🛡️ AI Based Security System using ESP32-CAM and YOLOv8

This sub-project focuses on an autonomous, real-time intruder detection system developed at **Mahendra Institute of Technology**[cite: 1, 2]. It integrates **Edge AI** with **IoT** for high-fidelity industrial or residential monitoring[cite: 1].

## 📝 Project Overview
Traditional surveillance systems often suffer from high false-positive rates due to simple motion detection[cite: 1]. Our system leverages the **YOLOv8** deep learning model to specifically identify human presence, ensuring that alerts are only triggered when an actual intruder is detected[cite: 1].

### 🚀 Key Features
*   **Intelligent Human Detection:** Uses YOLOv8 with an 80% confidence threshold to minimize false alarms[cite: 1].
*   **Live Web Streaming:** Flask-based server allows real-time monitoring via any mobile browser (1.8s latency)[cite: 1].
*   **Multi-Channel Alerting:**
    *   📸 **Telegram:** Instant photo capture with timestamp[cite: 1].
    *   📞 **Twilio:** Automatic emergency voice call to the owner[cite: 1].
    *   🚨 **Hardware:** Local LED/Buzzer activation via ESP32 GPIO[cite: 1].
*   **Periodic Surveillance:** Automated "Status: SAFE" heartbeat messages sent every 5 minutes[cite: 1].

## 📊 Performance Analysis
| Metric | Results |
| :--- | :--- |
| **Detection Accuracy** | **94.2%**[cite: 1] |
| **False Positive Rate** | **3.8%**[cite: 1] |
| **Response Latency** | **< 2.5 Seconds**[cite: 1] |
| **Alert Success Rate** | **99.3%**[cite: 1] |

## 🛠️ System Architecture
The system operates on a 4-Layer distributed design:
1.  **Input Layer:** ESP32-CAM captures and transmits images via WiFi[cite: 1].
2.  **Communication Layer:** Compressed frames sent via HTTP/MQTT protocol[cite: 1].
3.  **Processing Layer:** Python server performs YOLOv8 inference[cite: 1].
4.  **Output Layer:** Triggers Telegram, LED, and Twilio Voice API[cite: 1].



## 💻 Hardware & Software Requirements
*   **Hardware:** ESP32-CAM, FTDI Programmer, 5V DC Power Supply, LED[cite: 1].
*   **Software:** Python 3.14, Arduino IDE, Ultralytics (YOLOv8), Flask, Twilio & Telegram APIs[cite: 1].

## 👥 Contributors
*   **Nishanth M** - Project Lead & Developer[cite: 1]
**   **Supervisor:** Mrs. V. Annapoorani, M.E., Assistant Professor/ECE[cite: 1]

---

