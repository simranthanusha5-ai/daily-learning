"""Day 145: Bloom Filter implementation."""
import hashlib

class BloomFilter:
    def __init__(self, size=1000, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item):
        hashes = []
        for seed in range(self.num_hashes):
            data = f"{seed}:{item}".encode()
            digest = int(hashlib.sha256(data).hexdigest(), 16)
            hashes.append(digest % self.size)
        return hashes

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def __contains__(self, item):
        return all(self.bit_array[h] == 1 for h in self._hashes(item))

if __name__ == "__main__":
    bf = BloomFilter()
    bf.add("alice")
    bf.add("bob")
    assert "alice" in bf
    assert "bob" in bf
    assert "charlie" not in bf
    print("Day 145 Bloom Filter tests passed!")
