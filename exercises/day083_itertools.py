# Day 83: Itertools Module
import itertools

items = ["A", "B", "C"]
print("Permutations of 2:", list(itertools.permutations(items, 2)))
print("Combinations of 2:", list(itertools.combinations(items, 2)))
print("Accumulate sums:", list(itertools.accumulate([1, 2, 3, 4, 5])))
