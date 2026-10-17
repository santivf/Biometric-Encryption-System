import json
import numpy as np
from crypto_manager import store_user_vector, decrypt_vector

if __name__ == "__main__":
    user_vector = np.random.default_rng(42).random(128)
    store_user_vector("user_01", user_vector)
    with open("data/encrypted_data.json") as stream:
        data = json.load(stream)
    decrypted = decrypt_vector(data["user_01"])
    print("Ephemeral key: recovery is limited to this process.")
    print("Round-trip matches:", np.array_equal(user_vector, decrypted))
