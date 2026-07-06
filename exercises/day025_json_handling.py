# Day 25: JSON Handling
import json

payload = {
    "repository": "daily-learning",
    "owner": "simranthanusha5-ai",
    "stats": {"stars": 1, "commits": 100},
    "topics": ["python", "algorithms", "data-structures"],
    "published": True
}

# Serialize with clean indentation
json_str = json.dumps(payload, indent=2)
print("Serialized JSON:\n", json_str)

# Parse JSON string back to Python dict
parsed = json.loads(json_str)
assert parsed["owner"] == "simranthanusha5-ai"
print("Parsed repository successfully:", parsed["repository"])
