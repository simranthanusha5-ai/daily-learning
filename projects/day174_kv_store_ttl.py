"""Day 174: Key-Value Store with TTL."""
import time

class KeyValueStore:
    def __init__(self):
        self._store = {}
        self._expiry = {}

    def set(self, key, value, ttl_seconds=None):
        self._store[key] = value
        if ttl_seconds is not None:
            self._expiry[key] = time.time() + ttl_seconds
        elif key in self._expiry:
            del self._expiry[key]

    def get(self, key):
        if key in self._expiry and time.time() > self._expiry[key]:
            del self._store[key]
            del self._expiry[key]
            return None
        return self._store.get(key)

    def cleanup(self):
        now = time.time()
        expired = [k for k, exp in self._expiry.items() if exp < now]
        for k in expired:
            self._store.pop(k, None)
            self._expiry.pop(k, None)

if __name__ == "__main__":
    kv = KeyValueStore()
    kv.set("token", "xyz", ttl_seconds=0.01)
    assert kv.get("token") == "xyz"
    time.sleep(0.02)
    assert kv.get("token") is None
    print("Day 174 KV Store tests passed!")
