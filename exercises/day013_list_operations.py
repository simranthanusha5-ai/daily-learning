# Day 13: List Operations

tasks = ["plan", "code", "test"]
tasks.append("deploy")
tasks.extend(["monitor", "iterate"])
tasks.insert(1, "review_specs")

print("Initial tasks:", tasks)

# Removing elements
completed = tasks.pop(0)
print(f"Completed: {completed}, Remaining: {tasks}")

# Sorting
scores = [45, 12, 89, 78, 23, 56]
scores.sort(reverse=True)
print("Scores descending:", scores)
