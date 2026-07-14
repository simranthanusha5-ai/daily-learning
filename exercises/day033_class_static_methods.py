# Day 33: @classmethod and @staticmethod

class User:
    total_users = 0

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        User.total_users += 1

    @classmethod
    def from_csv_string(cls, data: str):
        name, email = data.split(",")
        return cls(name.strip(), email.strip())

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email

u1 = User("Alice", "alice@example.com")
u2 = User.from_csv_string("Bob, bob@example.com")

print(f"Total registered users: {User.total_users}")
print("Email validation test:", User.is_valid_email("test@domain.com"))
