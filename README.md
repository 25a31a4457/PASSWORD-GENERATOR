# PASSWORD-GENERATOR
A PROJECT IN PYTHON BASED ON PASSWORD GENERATION
# 🔐 Secure Password System (Python)

A simple and secure Password Generator & Strength Checker built using Python.  
This project allows users to generate strong passwords or check the strength of their own passwords.

## 📌 Features
- Generate secure random passwords
- Ensures password contains:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Check password strength (Weak / Medium / Strong)
- User-friendly menu system
- Input validation handling

## 🛠️ Technologies Used
- Python 3
- secrets module (for secure random generation)
- string module
- random module

## 📂 How It Works

### 1️⃣ Generate Password
- User enters desired password length (minimum 4).
- The system generates a secure password using secrets.choice().
- The password is shuffled for better randomness.

### 2️⃣ Check Password Strength
The program evaluates:
- Length (>= 8)
- Contains uppercase letters
- Contains lowercase letters
- Contains digits
- Contains special characters

### Strength Levels
- 0–2 → Weak
- 3–4 → Medium
- 5 → Strong

## ▶️ How to Run
1. Make sure Python 3 is installed.
2. Save the file as `password_system.py`.
3. Run the program:
