# Pass Generator 🔐

This is a terminal-based password manager written in Python. It allows users to securely add, view, and remove passwords using Caesar Cipher encryption, as well as generate and validate strong passwords.

## ✨ Features

- Add and encrypt new passwords (saved to `passwords.txt`)
- View stored passwords with decryption
- Remove specific service passwords
- Generate strong passwords based on security requirements
- Validate password strength (length, uppercase, lowercase, digits, special chars)
- Caesar Cipher encryption with a shift of 3

## 🚀 How It Works

Passwords are stored in an encrypted format using Caesar Cipher and written to a local file:

When viewing passwords, they are decrypted and printed in the terminal.

⚠️ **Note**: Caesar Cipher is for demonstration only and not secure for real-world password storage.

## 📦 Requirements

- Python 3.x  
(No external packages required)

## 🧪 Run the script

```bash
python Pass_Generator.py
