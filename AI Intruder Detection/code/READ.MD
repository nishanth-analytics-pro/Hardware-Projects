# 🛡️ AI Based Security System using ESP32-CAM and YOLOv8

This project is an autonomous, real-time intruder detection system developed at **Mahendra Institute of Technology**[cite: 1, 2]. It integrates **Edge AI** with **IoT** for high-fidelity industrial and residential monitoring.

---

## 📂 Project Resources & Documentation
Access the full project documentation and source files using the links below:

*   📄 **Final Project Report:** [Download/View Report](./FINALREPORTNISHANTH.doc)[cite: 1]
*   📊 **Project Presentation (PPT):** [Download/View PPT](./finalllllll1.pptx)[cite: 1]
*   💻 **Python Server Code:** [human_detection.py](./human_detection.py)[cite: 1]
*   🔌 **ESP32 Firmware:** [firmware.ino](./firmware.ino)[cite: 1]

---

## 📝 Project Overview
Traditional surveillance systems often suffer from high false-positive rates due to basic motion detection. Our system leverages the **YOLOv8** deep learning model to specifically identify human presence, ensuring that alerts are only triggered when an actual intruder is detected[cite: 1].

### 🚀 Key Features
*   **Intelligent Human Detection:** Uses YOLOv8 with an 80% confidence threshold to minimize false alarms[cite: 1].
*   **Live Web Streaming:** Flask-based server allows real-time monitoring via any mobile browser with minimal latency[cite: 1].
*   **Multi-Channel Alerting:**
    *   📸 **Telegram:** Instant photo capture with timestamp[cite: 1].
    *   📞 **Twilio:** Automatic emergency voice call to the owner[cite: 1].
    *   🚨 **Hardware:** Local LED/Buzzer activation via ESP32 GPIO[cite: 1].
*   **Periodic Surveillance:** Automated "Status: SAFE" heartbeat messages sent every 5 minutes[cite: 1].

---

## 📊 Performance Analysis
| Metric | Results |
| :--- | :--- |
| **Detection Accuracy** | **94.2%**[cite: 1] |
| **False Positive Rate** | **3.8%**[cite: 1] |
| **Response Latency** | **< 2.5 Seconds**[cite: 1] |
| **Alert Success Rate** | **99.3%**[cite: 1] |

---

## 🛠️ System Architecture
The system operates on a 4-Layer distributed design[cite: 1]:
1.  **Input Layer:** ESP32-CAM captures and transmits images via WiFi[cite: 1].
2.  **Communication Layer:** Compressed frames sent via HTTP protocol[cite: 1].
3.  **Processing Layer:** Python server performs YOLOv8 inference[cite: 1].
4.  **Output Layer:** Triggers Telegram, LED, and Twilio Voice API[cite: 1].

---

## 👥 Contributors
*   **Nishanth M** - Project Lead & Developer[cite: 1]
*   **Mukesh M** - Hardware Integration[cite: 1]
*   **Prasanna P** - Testing & Documentation[cite: 1]
*   **Pugatheeshwaran** - Alert Logic Design[cite: 1]
*   **Supervisor:** Mrs. V. Annapoorani, M.E., Assistant Professor/ECE[cite: 1]

---

## 📜 Academic Credits
Developed as part of the academic curriculum at **Mahendra Institute of Technology (Autonomous)**[cite: 1, 2].
