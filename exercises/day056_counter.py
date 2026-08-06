# Day 56: collections.Counter & defaultdict
from collections import Counter, defaultdict

text = "apple banana apple cherry apple banana kiwi"
counts = Counter(text.split())
print("Word frequencies:", counts)
print("Top 2 most common:", counts.most_common(2))

# Grouping words by length using defaultdict
grouped = defaultdict(list)
for word in text.split():
    grouped[len(word)].append(word)
print("Grouped by length:", dict(grouped))
