 Encrypted Python Keylogger (PoC)

This is a project I built to explore how malware works, specifically focusing on encryption and remote logging (C2). It’s a Proof of Concept (PoC) showing how keystrokes can be captured, encrypted, and sent to a server.

> **Disclaimer:** This is for **educational purposes only**. Please don't use this on any machine you don't own. I'm not responsible for what you do with it.

---

# What is inside?

The system is split into 4 simple parts:

1.  **server.py**: The "brain" (C2). It uses Flask to listen for incoming data and saves it to a text file.
2.  **payload.py**: The actual keylogger. It records keys and sends them to the server.
3.  **builder.py**: This is the encryption tool. It turns your plain code into an encrypted mess so it's harder to analyze.
4.  **loader.py**: The "starter". It sits on the target machine, decrypts the payload in memory (RAM), and adds itself to Windows Startup for persistence.

---

# How to use it?

**1. Install the basics:**
Open your terminal and run:
```
pip install flask cryptography pynput requests

2. Start the Server:
Run this first so it's ready to catch the logs:

python server.py

3. Encrypt the Payload:
Run builder.py. It will give you an Encryption Key and a long string of Encrypted Data in the terminal.

4. Setup the Loader:
Open loader.py and paste the Key and Encrypted Data into the variables at the top.

5. Deploy & Test:
Run loader.py on a Windows machine. It will automatically hide in the Startup folder and start working in the background.
🛡️ Why this method?

I used Fernet (AES) encryption here. The real code is never saved as plain text on the hard drive—it only decrypts inside the RAM. This is a common way to avoid basic static antivirus scans.

Made by:  Dragon
