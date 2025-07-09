# Caesar-Cipher-Implementation-Guide

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

## 🏗️ Folder Structure


caesar_cipher_tool/
├── caesar_cipher_tool.py
├── input_module.py
├── encryptor.py
├── decryptor.py
├── display.py
├── file_writer.py
└── output.txt  # (generated after run)


---

## ▶️ How to Run

1. Clone the repository or extract the `.zip` file.
2. Open the terminal or command prompt.
3. Navigate to the folder:
   ```bash
   cd caesar_cipher_tool

Run the main script:

python caesar_cipher_tool.py

Example Walkthrough

Input:
Enter the text: HELLO WORLD

Enter the shift key: 5

Output:

Encrypted Text: MJQQT BTWQI
Decrypted Text: HELLO WORLD
Encrypted text saved to: output.txt


📁 Output File

After successful encryption, the tool writes the encrypted text to output.txt, which can be found in the same folder.

Example:

MJQQT BTWQI

🔒 Encryption Logic Explained :-

For each character in the input string:

If it’s an alphabet:

Calculate its position in the alphabet (A-Z or a-z).

Add the shift key value.

Use modulo 26 to wrap around.

If it’s not an alphabet (space, punctuation), keep it as-is.

🔓 Decryption Logic Explained :-

Same as encryption but subtract the key instead of adding.

This is done by calling encrypt(text, -key).


✅ Features :-

Accepts both uppercase and lowercase inputs.

Leaves numbers, symbols, and spaces unchanged.

Properly handles wrap-around cases (e.g., Z + 1 → A).

Clean, modular code using Python functions and files.

Easy to extend or customize.

📚 Learning Outcomes :-

Understanding of Caesar Cipher principles

Modular Python programming

File handling (read/write)

String manipulation

Clean project structuring


🚀 Possible Enhancements :-

Add GUI (Tkinter or web-based)

Support for Unicode characters

Add brute-force attack mode (try all 26 shifts)

Add frequency analysis for decryption without key

🧾 Conclusion :-

This project demonstrates how classical encryption can be implemented using modern programming practices. The Caesar Cipher tool is a simple but powerful example of modular design and cryptographic logic, suitable for academic learning and beginner cryptography understanding.


👨‍💻 Author :-
Name: Jonnalagadda Suresh
Course: 
Professor: 
Submission Date: [Add Date]
