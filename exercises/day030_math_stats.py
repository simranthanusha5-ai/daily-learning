# Day 30: Math, Random & Statistics
import statistics
import random

random.seed(42)
scores = [random.randint(50, 100) for _ in range(15)]
print("Generated scores:", scores)

print(f"Mean:   {statistics.mean(scores):.2f}")
print(f"Median: {statistics.median(scores):.2f}")
print(f"StDev:  {statistics.stdev(scores):.2f}")
