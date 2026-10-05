"""Day 139: ThreadPoolExecutor with Future Callbacks."""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def compute_square(n):
    return n * n

def test_executor():
    results = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(compute_square, x): x for x in range(5)}
        for future in as_completed(futures):
            results.append(future.result())
    return sorted(results)

if __name__ == "__main__":
    res = test_executor()
    assert res == [0, 1, 4, 9, 16]
    print("Day 139 ThreadPoolExecutor tests passed!")
