import os
import tempfile
import unittest
from pathlib import Path

class TemporaryDirectoryTest(unittest.TestCase):
    def setUp(self):
        self.cwd = Path.cwd()
        self.temp = tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)

    def tearDown(self):
        os.chdir(self.cwd)
        self.temp.cleanup()

import json
import numpy as np
from cryptography.fernet import Fernet, InvalidToken
from crypto_manager import store_user_vector, decrypt_vector, encrypt_vector

class CryptoTests(TemporaryDirectoryTest):
    def test_fresh_directory_round_trip(self):
        vector = np.array([0.1, 0.2, 0.3])
        store_user_vector("demo", vector)
        token = json.loads(Path("data/encrypted_data.json").read_text())["demo"]
        np.testing.assert_array_equal(vector, decrypt_vector(token))

    def test_another_key_cannot_recover_token(self):
        token = encrypt_vector(np.array([1.]))
        with self.assertRaises(InvalidToken):
            Fernet(Fernet.generate_key()).decrypt(token.encode())

    def test_second_write_replaces_previous_user(self):
        store_user_vector("first", np.array([1.]))
        store_user_vector("second", np.array([2.]))
        self.assertEqual(list(json.loads(Path("data/encrypted_data.json").read_text())), ["second"])
