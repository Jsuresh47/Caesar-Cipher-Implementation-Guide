# 📜 Caesar Cipher Encoder/Decoder Tool – Project Documentation

## 🔍 Project Title
**Caesar Cipher Text Encryption/Decryption Utility**

---

## 🎯 Objective
The primary objective of this project is to develop a simple yet effective text encryption and decryption tool using the **Caesar Cipher** algorithm. The tool allows users to:
- Input plaintext and a shift key
- Encrypt the text using Caesar Cipher logic
- Decrypt the encrypted text using the same key
- Display the result in a user-friendly format
- Save the encrypted output to a `.txt` file

---

## 🧠 What is Caesar Cipher?
Caesar Cipher is a classical encryption technique named after Julius Caesar, who used it to protect his confidential messages. It involves shifting each letter in a message by a fixed number of positions in the alphabet.

For example:
- Original Text: `HELLO`
- Shift Key: `3`
- Encrypted Text: `KHOOR`

It’s a substitution cipher and forms the foundation of many modern cryptographic techniques.

---

## 🧩 Project Modules

To maintain clean code and modularity, the project is divided into **five functional modules** plus a main script:

### 1. `input_module.py`
Handles user input. Accepts the text and numeric shift key from the user via command line.

### 2. `encryptor.py`
Performs Caesar Cipher encryption by shifting characters forward by the key value.

### 3. `decryptor.py`
Uses the same Caesar Cipher logic in reverse to recover the original message.

### 4. `display.py`
Formats and displays both the encrypted and decrypted messages to the user.

### 5. `file_writer.py`
Saves the encrypted message to a file named `output.txt`.

### 6. `caesar_cipher_tool.py` (Main Script)
Acts as the main controller that imports functions from other modules and executes the workflow.

---

## 🛠️ Technologies Used
- **Language:** Python 3.x
- **IDE:** VS Code / PyCharm / Terminal
- **File I/O:** Standard Python open/read/write
- **No external libraries** are required

---

## 🏗️ Folder Structure

