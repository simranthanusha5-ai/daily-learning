# Day 71: Type Hints
from typing import Optional, Callable

def process_numbers(
    numbers: list[int],
    transform: Callable[[int], int],
    fallback: Optional[int] = None
) -> list[int]:
    if not numbers and fallback is not None:
        return [fallback]
    return [transform(n) for n in numbers]

doubled = process_numbers([1, 2, 3], lambda x: x * 2)
print("Doubled:", doubled)
