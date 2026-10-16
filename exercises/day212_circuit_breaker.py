"""Day 212: Circuit Breaker."""
import time

class CircuitBreakerOpenException(Exception): pass

class CircuitBreaker:
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

    def __init__(self, failure_thresh=3, reset_timeout=0.1):
        self.failure_thresh = failure_thresh
        self.reset_timeout = reset_timeout
        self.state = self.CLOSED
        self.failures = 0
        self.last_failure_time = 0

    def call(self, func, *args, **kwargs):
        now = time.time()
        if self.state == self.OPEN:
            if now - self.last_failure_time > self.reset_timeout:
                self.state = self.HALF_OPEN
            else:
                raise CircuitBreakerOpenException("Circuit is open")

        try:
            res = func(*args, **kwargs)
            if self.state == self.HALF_OPEN:
                self.state = self.CLOSED
                self.failures = 0
            return res
        except Exception as e:
            self.failures += 1
            self.last_failure_time = time.time()
            if self.failures >= self.failure_thresh:
                self.state = self.OPEN
            raise e

if __name__ == "__main__":
    cb = CircuitBreaker(failure_thresh=2, reset_timeout=0.05)
    def fail(): raise ValueError("down")
    for _ in range(2):
        try: cb.call(fail)
        except ValueError: pass
    assert cb.state == CircuitBreaker.OPEN
    time.sleep(0.06)
    def ok(): return 200
    assert cb.call(ok) == 200
    assert cb.state == CircuitBreaker.CLOSED
    print("Day 212 Circuit Breaker tests passed!")
