# Day 75: Parameterized Decorators
from functools import wraps

def repeat(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = [func(*args, **kwargs) for _ in range(times)]
            return results[-1]
        return wrapper
    return decorator

@repeat(times=3)
def greet(name: str):
    print(f"Hello, {name}!")

greet("Thanusha")
