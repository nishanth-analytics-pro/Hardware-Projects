from flask import Flask, Response
import cv2
import requests
import numpy as np
import time
import os  # Intha line kandippa irukanum
from ultralytics import YOLO
from datetime import datetime
from twilio.rest import Client

app = Flask(__name__)

# --- CONFIGURATION ---
ESP32_IP = "10.107.100.176" 
ESP32_CAM_URL = f"http://{ESP32_IP}/capture"
ESP32_CONTROL = f"http://{ESP32_IP}"

BOT_TOKEN = "8787883853:AAF0z4VH5CFcYWFsArMeLmu0SSU7NTHJxvw"
CHAT_ID = "6613482619"

account_sid = "AC532ecf85d00baa086b696eb4002fd21b"
auth_token = "6fb8554b4514b26002d45cfc0c1d91fd"
twilio_number = "+16413484574"
your_number = "+918248613536"

client = Client(account_sid, auth_token)
model = YOLO("yolov8n.pt") 

# --- CONTROL VARIABLES ---
last_alert_time = 0
last_periodic_check = time.time()
alert_cooldown = 25 
periodic_interval = 300 # 5 Minutes

def send_telegram_msg(message, image_path=None):
    try:
        if image_path:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
            with open(image_path, "rb") as img:
                requests.post(url, data={"chat_id": CHAT_ID, "caption": message, "parse_mode": "Markdown"}, files={"photo": img})
        else:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"})
    except Exception as e:
        print(f"Telegram Error: {e}")

def gen_frames():
    global last_alert_time, last_periodic_check
    
    while True:
        try:
            img_resp = requests.get(ESP32_CAM_URL, timeout=5)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
            if frame is None: continue

            current_time = time.time()
            results = model(frame, verbose=False, conf=0.80)
            person_detected = False

            for r in results:
                for box in r.boxes:
                    if int(box.cls[0]) == 0: 
                        person_detected = True
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.putText(frame, "UNKNOWN PERSON", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

            if person_detected:
                try: requests.get(f"{ESP32_CONTROL}/on", timeout=1)
                except: pass
                
                if current_time - last_alert_time > alert_cooldown:
                    ts = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                    if not os.path.exists("captures"): os.makedirs("captures")
                    img_name = f"captures/intruder_{int(current_time)}.jpg"
                    cv2.imwrite(img_name, frame)
                    
                    send_telegram_msg(f"🚨 *INTRUDER DETECTED!*\nTime: {ts}\nStatus: Calling Owner...", img_name)
                    client.calls.create(to=your_number, from_=twilio_number, url="http://demo.twilio.com/docs/voice.xml")
                    last_alert_time = current_time
            else:
                try: requests.get(f"{ESP32_CONTROL}/off", timeout=1)
                except: pass
                
                if current_time - last_periodic_check > periodic_interval:
                    ts = datetime.now().strftime("%I:%M %p")
                    send_telegram_msg(f"🛡️ *MIT SURVEILLANCE*\nStatus: All Safe\nTime: {ts}")
                    last_periodic_check = current_time

            ret, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

        except Exception as e:
            print(f"Loop Error: {e}")
            time.sleep(1)

@app.route('/')
def index():
    return "<h1>MIT Smart Surveillance Active</h1><img src='/video_feed' width='100%'>"

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    if not os.path.exists("captures"): os.makedirs("captures")
    app.run(host='0.0.0.0', port=5000, threaded=True)
