"""Day 184: Cuckoo Filter."""
import hashlib

class CuckooFilter:
    def __init__(self, capacity=128, bucket_size=4, max_kicks=20):
        self.capacity = capacity
        self.bucket_size = bucket_size
        self.max_kicks = max_kicks
        self.buckets = [[] for _ in range(capacity)]

    def _fingerprint(self, item):
        h = hashlib.sha256(item.encode()).digest()
        return (h[0] % 254) + 1

    def _hash(self, item):
        return int(hashlib.md5(item.encode()).hexdigest(), 16) % self.capacity

    def _alt_index(self, i1, fp):
        h = int(hashlib.md5(bytes([fp])).hexdigest(), 16) % self.capacity
        return (i1 ^ h) % self.capacity

    def insert(self, item):
        fp = self._fingerprint(item)
        i1 = self._hash(item)
        i2 = self._alt_index(i1, fp)

        if len(self.buckets[i1]) < self.bucket_size:
            self.buckets[i1].append(fp)
            return True
        if len(self.buckets[i2]) < self.bucket_size:
            self.buckets[i2].append(fp)
            return True

        curr_i = i1
        for _ in range(self.max_kicks):
            evicted_fp = self.buckets[curr_i].pop(0)
            self.buckets[curr_i].append(fp)
            fp = evicted_fp
            curr_i = self._alt_index(curr_i, fp)
            if len(self.buckets[curr_i]) < self.bucket_size:
                self.buckets[curr_i].append(fp)
                return True
        return False

    def contains(self, item):
        fp = self._fingerprint(item)
        i1 = self._hash(item)
        i2 = self._alt_index(i1, fp)
        return fp in self.buckets[i1] or fp in self.buckets[i2]

    def delete(self, item):
        fp = self._fingerprint(item)
        i1 = self._hash(item)
        i2 = self._alt_index(i1, fp)
        if fp in self.buckets[i1]:
            self.buckets[i1].remove(fp)
            return True
        if fp in self.buckets[i2]:
            self.buckets[i2].remove(fp)
            return True
        return False

if __name__ == "__main__":
    cf = CuckooFilter(capacity=32)
    assert cf.insert("apple") is True
    assert cf.contains("apple") is True
    assert cf.delete("apple") is True
    assert cf.contains("apple") is False
    print("Day 184 Cuckoo Filter tests passed!")
