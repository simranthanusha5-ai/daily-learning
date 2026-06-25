# Day 14: List Comprehensions

numbers = list(range(1, 21))

# Squares of even numbers
even_squares = [n**2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)

# Nested list flattening
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print("Flattened matrix:", flattened)

# Conditional expression in comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in range(6)]
print("Labels:", labels)
