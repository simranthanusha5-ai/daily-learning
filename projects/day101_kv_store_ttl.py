# Day 101 Project: Key-Value Store with TTL
import time

class TTLCache:
    def __init__(self):
        self.store = {}

    def set(self, key: str, val, ttl_seconds: float):
        expires_at = time.time() + ttl_seconds
        self.store[key] = (val, expires_at)

    def get(self, key: str):
        if key not in self.store:
            return None
        val, expires_at = self.store[key]
        if time.time() > expires_at:
            del self.store[key]
            return None
        return val

cache = TTLCache()
cache.set("session_token", "abc-123-xyz", ttl_seconds=10)
print("Cache hit:", cache.get("session_token"))
