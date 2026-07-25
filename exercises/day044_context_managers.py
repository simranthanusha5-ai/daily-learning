# Day 44: Context Managers
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed * 1000:.3f} ms")
        return False

with Timer():
    total = sum(i ** 2 for i in range(100000))
