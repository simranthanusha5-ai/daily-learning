# Day 43: Generator Expressions

import sys

# List comprehension: builds full list in memory
list_comp = [x * 2 for x in range(10000)]
# Generator expression: lazily computed
gen_exp = (x * 2 for x in range(10000))

print("List memory (bytes):", sys.getsizeof(list_comp))
print("Gen memory (bytes):", sys.getsizeof(gen_exp))

# Summing via generator without materializing
total = sum(x for x in range(101) if x % 2 == 0)
print("Sum of even numbers 0-100:", total)
