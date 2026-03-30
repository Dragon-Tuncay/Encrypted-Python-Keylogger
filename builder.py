from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("secret.key", "wb") as kf:
    kf.write(key)


with open("payload.py", "rb") as f:
    payload_raw = f.read()


cipher = Fernet(key)
encrypted_payload = cipher.encrypt(payload_raw)


with open("payload.enc", "wb") as f:
    f.write(encrypted_payload)

print("[+] 'payload.enc' and 'secret.key' created successfully.")
print("-" * 50)
print("Copy and paste these values into your 'loader.py':")
print(f"\nKEY = {key}")
print("\n" + "="*60 + "\n") 
print(f"ENCRYPTED_DATA = {encrypted_payload}")
print("-" * 50)
