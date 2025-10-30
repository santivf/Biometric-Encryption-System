import json, numpy as np
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_vector(vector):
    encoded = json.dumps(vector.tolist()).encode()
    return fernet.encrypt(encoded).decode()

def decrypt_vector(token):
    decoded = fernet.decrypt(token.encode())
    return np.array(json.loads(decoded))

def store_user_vector(user_id, vector):
    data = {user_id: encrypt_vector(vector)}
    with open("data/encrypted_data.json", "w") as f:
        json.dump(data, f, indent=4)

