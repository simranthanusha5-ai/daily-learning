# Day 42: Generators and yield

def fibonacci(limit: int):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

fib_seq = list(fibonacci(10))
print("First 10 Fibonacci numbers:", fib_seq)
