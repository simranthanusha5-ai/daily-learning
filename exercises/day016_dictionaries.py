# Day 16: Dictionaries Deep Dive

user = {
    "username": "thanusha",
    "role": "engineer",
    "skills": ["python", "git"]
}

# Safe lookup with .get()
location = user.get("location", "Not specified")
print(f"User location: {location}")

# setdefault to initialize missing keys
user.setdefault("projects_completed", []).append("daily-learning")

# Iterating keys and values
for key, val in user.items():
    print(f"{key}: {val}")
