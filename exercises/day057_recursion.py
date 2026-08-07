# Day 57: Recursion

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sum_array(arr: list[int]) -> int:
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])

print("Factorial of 5:", factorial(5))
print("Sum of [1, 2, 3, 4, 5]:", sum_array([1, 2, 3, 4, 5]))
