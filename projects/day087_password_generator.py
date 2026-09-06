# Day 87 Project: Password Generator and Validator
import secrets
import string

def generate_secure_password(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    while True:
        pwd = "".join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in pwd)
            and any(c.isupper() for c in pwd)
            and any(c.isdigit() for c in pwd)
            and any(c in "!@#$%^&*()-_=+" for c in pwd)):
            return pwd

def check_strength(password: str) -> str:
    score = 0
    if len(password) >= 12: score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    return "Strong" if score >= 4 else "Moderate" if score >= 2 else "Weak"

pwd = generate_secure_password(16)
print(f"Generated Password: {pwd} | Strength: {check_strength(pwd)}")
