# Day 23: Higher-Order Functions
from functools import reduce

prices = [10.5, 25.0, 5.75, 42.0, 15.2]

# Filter items over $15
expensive = list(filter(lambda p: p > 15.0, prices))
print("Expensive items:", expensive)

# Map discount of 10%
discounted = list(map(lambda p: round(p * 0.9, 2), prices))
print("Discounted prices:", discounted)

# Reduce to total sum
total = reduce(lambda acc, p: acc + p, prices, 0)
print(f"Total: ${total:.2f}")

# Enumerate and Zip
labels = ["Book", "Game", "Pen", "Headphones", "Notebook"]
for idx, (label, price) in enumerate(zip(labels, prices), start=1):
    print(f"{idx}. {label}: ${price:.2f}")
