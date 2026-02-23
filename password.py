import secrets
import string
import random
def secure_password(length):
    if length < 4:
        return "Length must be at least 4"
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    all_characters = string.ascii_letters + string.digits + string.punctuation
    for i  in range(length - 4):
        password.append(secrets.choice(all_characters))
    random.shuffle(password)
    return "".join(password)
def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
print("------ Secure Password System ------")
while True:
    print("1. Generate Password")
    print("2. Create Your Own Password")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        try:
            length = int(input("Enter password length: "))
            print("Generated Password:", secure_password(length))
        except ValueError:
            print("Invalid Input!Try Again...")
    elif choice == "2":

        
        while True:
            user_password = input("Enter your password: ").strip()

            if not user_password:
                print("Please enter a password")
            else:
                break 

        print("Password Strength:", check_strength(user_password))
        
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!Try Again..")