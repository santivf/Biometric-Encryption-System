import numpy as np
from crypto_manager import store_user_vector, decrypt_vector, fernet

    #create biometric vector
user_vector = np.random.rand(128)

    #save encryption
store_user_vector("user_01", user_vector)

    #read and decipher
from json import load
with open("data/encrypted_data.json") as f:
    data = load(f)
decrypted = decrypt_vector(data["user_01"])

print("Original vector (first 5):", user_vector[:5])
print("Decrypted vector (first 5):", decrypted[:5])


