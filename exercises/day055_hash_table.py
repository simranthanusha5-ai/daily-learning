# Day 55: Hash Table with Separate Chaining

class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        return sum(ord(c) for c in key) % self.size

    def put(self, key: str, value):
        bucket = self.buckets[self._hash(key)]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: str):
        bucket = self.buckets[self._hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        return None

ht = HashTable()
ht.put("python", 3.12)
ht.put("git", 2.45)
print("Lookup 'python':", ht.get("python"))
