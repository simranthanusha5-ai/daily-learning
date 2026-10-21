"""Day 257: Sliding Window Log Limiter."""
import time

class SlidingWindowLogLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window = window_seconds
        self.logs = []

    def allow(self):
        now = time.time()
        boundary = now - self.window
        self.logs = [t for t in self.logs if t > boundary]
        if len(self.logs) < self.max_requests:
            self.logs.append(now)
            return True
        return False

if __name__ == "__main__":
    lim = SlidingWindowLogLimiter(2, 0.1)
    assert lim.allow() is True
    assert lim.allow() is True
    assert lim.allow() is False
    time.sleep(0.12)
    assert lim.allow() is True
    print("Day 257 Sliding Window Limiter tests passed!")
