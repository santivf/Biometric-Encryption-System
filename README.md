# Biometric Encryption System
A secure simulation for encrypting and decrypting biometric vectors using symmetric cryptography.

## Overview
This project demonstrates how to safely store and verify biometric data by encrypting feature vectors with **Fernet (AES-based)** encryption.  
It prevents exposure of sensitive information during storage or transmission.

## Features
- AES-based encryption and decryption  
- JSON data storage  
- Secure key generation and vector handling  
- Modular cryptography functions  

## Technologies Used
- **Python**
- **cryptography**
- **NumPy**
- **JSON**

## Installation
```bash
pip install cryptography numpy json5

## Usage
- Run main.py.
- The script encrypts and stores a biometric vector in JSON format.
- It then decrypts the vector and verifies that both are identical.

## Project Structure
biometric_encryption_system/
├── main.py
├── crypto_manager.py
├── data/
│   └── encrypted_data.json
├── requirements.txt
└── README.md

## Scalability
- Can evolve into:
- Secure biometric databases
- Multi-user authentication systems
- Encrypted identity validation services