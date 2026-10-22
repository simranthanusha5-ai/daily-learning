"""Day 271: Mini Redis Engine."""
import time

class MiniRedis:
    def __init__(self):
        self._strings = {}
        self._hashes = {}
        self._expirations = {}

    def set(self, key, value, ex=None):
        self._strings[key] = value
        if ex:
            self._expirations[key] = time.time() + ex
        elif key in self._expirations:
            del self._expirations[key]

    def get(self, key):
        if key in self._expirations and time.time() > self._expirations[key]:
            del self._strings[key]
            del self._expirations[key]
            return None
        return self._strings.get(key)

    def hset(self, name, key, value):
        if name not in self._hashes:
            self._hashes[name] = {}
        self._hashes[name][key] = value

    def hget(self, name, key):
        return self._hashes.get(name, {}).get(key)

if __name__ == "__main__":
    r = MiniRedis()
    r.set("k1", "v1")
    assert r.get("k1") == "v1"
    r.hset("user:1", "name", "Thanusha")
    assert r.hget("user:1", "name") == "Thanusha"
    print("Day 271 Mini Redis tests passed!")
