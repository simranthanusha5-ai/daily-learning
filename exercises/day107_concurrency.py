# Day 107: Concurrency Concepts
import concurrent.futures

def square_num(n: int) -> int:
    return n * n

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    numbers = [1, 2, 3, 4, 5, 6]
    results = list(executor.map(square_num, numbers))

print("Concurrent ThreadPool results:", results)
