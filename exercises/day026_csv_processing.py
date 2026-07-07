# Day 26: CSV Processing
import csv
import io

data = [
    {"day": 1, "topic": "GitHub Basics", "status": "completed"},
    {"day": 2, "topic": "Branching", "status": "completed"},
    {"day": 3, "topic": "Python Intro", "status": "in-progress"},
]

# Write CSV to memory buffer
output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=["day", "topic", "status"])
writer.writeheader()
writer.writerows(data)

csv_content = output.getvalue()
print("CSV Output:\n" + csv_content.strip())

# Read back
reader = csv.DictReader(io.StringIO(csv_content))
rows = list(reader)
print(f"Successfully processed {len(rows)} CSV records.")
