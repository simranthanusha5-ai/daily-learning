# Day 22: Lambda Functions

students = [
    {"name": "Alice", "grade": 88, "age": 20},
    {"name": "Bob", "grade": 95, "age": 22},
    {"name": "Charlie", "grade": 72, "age": 19},
]

# Sorting by grade descending
by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print("Top students by grade:", [s["name"] for s in by_grade])

# Multi-criteria sort (by age, then by name)
by_age = sorted(students, key=lambda s: (s["age"], s["name"]))
print("Sorted by age:", [(s["name"], s["age"]) for s in by_age])
