# Day 18: Sets and Set Operations

frontend = {"HTML", "CSS", "JavaScript", "TypeScript"}
backend = {"Python", "JavaScript", "SQL", "Docker"}

print("Union (All skills):", frontend | backend)
print("Intersection (Shared):", frontend & backend)
print("Difference (Frontend only):", frontend - backend)
print("Symmetric Difference (Exclusive):", frontend ^ backend)

# Fast deduplication
tags = ["python", "git", "python", "ai", "git", "cloud"]
unique_tags = sorted(list(set(tags)))
print("Unique tags:", unique_tags)
