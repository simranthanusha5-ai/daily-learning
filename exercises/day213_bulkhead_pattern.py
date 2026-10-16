"""Day 213: Bulkhead Pattern."""
import threading

class Bulkhead:
    def __init__(self, max_concurrent=2):
        self.semaphore = threading.Semaphore(max_concurrent)

    def execute(self, task):
        acquired = self.semaphore.acquire(blocking=False)
        if not acquired:
            raise RuntimeError("Bulkhead capacity reached")
        try:
            return task()
        finally:
            self.semaphore.release()

if __name__ == "__main__":
    bh = Bulkhead(max_concurrent=1)
    res = bh.execute(lambda: 42)
    assert res == 42
    print("Day 213 Bulkhead tests passed!")
