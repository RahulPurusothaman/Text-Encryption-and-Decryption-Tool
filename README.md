# 🔐 Message Encryption and Decryption Project

This project is a basic encryption and decryption tool using the `cryptography` library's `Fernet` module. The tool allows users to securely encrypt a message using a randomly generated key and then decrypt the message with the correct key.

## ✨ Features
- 🔑 Generate a custom-length encryption key.
- 🛡️ Encrypt any message using the generated key.
- 🔓 Decrypt the encrypted message with the correct key.
- 🔐 Basic password/key verification to ensure only authorized decryption.

## ⚙️ How It Works

### 🔑 Key Generation
The user is prompted to provide the length of the encryption key, which is then generated using a random selection of characters from a predefined set of alphanumeric characters.

### 🛡️ Message Encryption
The user inputs a message to be encrypted. The program uses the `cryptography` library to encrypt the message using the randomly generated key. The encrypted message is then displayed.

### 🔓 Message Decryption
The program prompts the user to input the correct key to decrypt the message. If the key matches, the original message is decrypted and shown. If the key is incorrect, the decryption fails with an error message.

## 🛠️ Prerequisites

Before running the project, ensure that you have installed the required Python libraries:

```bash
pip install cryptography


🚀 Usage:

💻 Clone the repository or download the script.
🏃 Run the Python script.
🔑 Enter the desired length for the encryption key.
✍️ Input the message you want to encrypt.
📝 Copy the generated encryption key.
🔓 Provide the key when prompted for decryption.


