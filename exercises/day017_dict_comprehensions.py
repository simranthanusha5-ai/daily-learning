# Day 17: Dict Comprehensions and Merging

words = ["python", "programming", "daily", "streak"]
lengths = {w: len(w) for w in words}
print("Word lengths:", lengths)

# Inverted mapping
inverted = {v: k for k, v in lengths.items()}
print("Inverted:", inverted)

# Python 3.9+ Dictionary Merge Operator (|)
defaults = {"theme": "dark", "notifications": True, "font_size": 14}
custom = {"font_size": 16, "theme": "system"}
config = defaults | custom
print("Merged config:", config)
