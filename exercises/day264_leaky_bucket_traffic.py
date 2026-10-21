"""Day 264: Leaky Bucket Shaper."""
import time

class LeakyBucket:
    def __init__(self, capacity=10, leak_rate=2):
        self.capacity = capacity
        self.leak_rate = leak_rate # units leaked per second
        self.water = 0.0
        self.last_leak = time.time()

    def _leak(self):
        now = time.time()
        elapsed = now - self.last_leak
        self.water = max(0.0, self.water - elapsed * self.leak_rate)
        self.last_leak = now

    def add(self, amount=1):
        self._leak()
        if self.water + amount <= self.capacity:
            self.water += amount
            return True
        return False

if __name__ == "__main__":
    lb = LeakyBucket(capacity=2, leak_rate=5)
    assert lb.add(2) is True
    assert lb.add(1) is False
    time.sleep(0.25)
    assert lb.add(1) is True
    print("Day 264 Leaky Bucket tests passed!")
