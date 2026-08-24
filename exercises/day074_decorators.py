# Day 74: Function Decorators
from functools import wraps
import time

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}'...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Finished '{func.__name__}' in {duration * 1000:.2f} ms")
        return result
    return wrapper

@log_execution
def compute_cube_sum(limit: int) -> int:
    return sum(i ** 3 for i in range(limit))

print("Result:", compute_cube_sum(50000))
