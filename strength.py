import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Lowercase check
    if re.search("[a-z]", password):
        score += 1

    # Uppercase check
    if re.search("[A-Z]", password):
        score += 1

    # Digit check
    if re.search("[0-9]", password):
        score += 1

    # Special character check
    if re.search("[@#$%^&*()_+=!]", password):
        score += 1

    # Strength evaluation
    if score <= 2:
        return "Weak Password ❌"
    elif score == 3 or score == 4:
        return "Moderate Password ⚠️"
    else:
        return "Strong Password ✅"


# User input
password = input("Enter your password: ")

strength = check_password_strength(password)

print("Password Strength:", strength)