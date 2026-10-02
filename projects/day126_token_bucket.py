# Day 126 Project: Token Bucket API Rate Limiter
import time

class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec
        self.tokens = float(capacity)
        self.last_refill = time.time()

    def _refill(self):
        now = time.time()
        delta = now - self.last_refill
        self.tokens = min(float(self.capacity), self.tokens + (delta * self.refill_rate))
        self.last_refill = now

    def allow_request(self, tokens_needed: int = 1) -> bool:
        self._refill()
        if self.tokens >= tokens_needed:
            self.tokens -= tokens_needed
            return True
        return False

limiter = TokenBucketRateLimiter(capacity=3, refill_rate_per_sec=1.0)
print("Request 1 allowed:", limiter.allow_request())
print("Request 2 allowed:", limiter.allow_request())
print("Request 3 allowed:", limiter.allow_request())
print("Request 4 allowed (should throttle):", limiter.allow_request())
