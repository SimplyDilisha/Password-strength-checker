# 🔐 Password Strength Checker (Python)

A simple Python program that checks the **strength of a password** based on multiple security criteria such as length, uppercase letters, lowercase letters, numbers, and special characters.

This project helps users understand whether their password is **Weak, Moderate, or Strong**.

---

## 🚀 Features

* Checks password length
* Detects uppercase and lowercase characters
* Detects numbers
* Detects special symbols
* Classifies password strength into:

  * ❌ Weak
  * ⚠️ Moderate
  * ✅ Strong

---

## 🛠️ Technologies Used

* Python
* `re` (Regular Expressions)

---

## 📂 Project Structure

```
password-strength-checker/
│
├── password_checker.py
└── README.md
```

---

## 📜 Code

```python
import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[@#$%^&*()_+=!]", password):
        score += 1

    if score <= 2:
        return "Weak Password ❌"
    elif score == 3 or score == 4:
        return "Moderate Password ⚠️"
    else:
        return "Strong Password ✅"

password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
```

---

## ▶️ How to Run

1. Install Python (if not installed).
2. Download or clone this repository.

```bash
git clone https://github.com/yourusername/password-strength-checker.git
```

3. Navigate to the project folder.

```bash
cd password-strength-checker
```

4. Run the Python file.

```bash
python password_checker.py
```

---

## 💻 Example Output

```
Enter your password: Hello123
Password Strength: Moderate Password ⚠️
```

```
Enter your password: H@rdPass123
Password Strength: Strong Password ✅
```

---

## 🎯 Future Improvements

* Add **password strength score (0–100)**
* Create a **GUI version using Tkinter**
* Build a **password generator + strength checker**
* Add a **visual strength meter**

---

## 📄 License

This project is open source and free to use.

---

