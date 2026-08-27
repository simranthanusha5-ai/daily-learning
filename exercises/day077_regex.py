# Day 77: Regular Expressions Fundamentals
import re

email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

emails = ["user@example.com", "valid.name+tag@sub.domain.org", "bad_email@"]
for email in emails:
    valid = bool(re.match(email_pattern, email))
    print(f"'{email}' is valid email: {valid}")
