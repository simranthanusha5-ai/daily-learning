"""Day 183: Count-Min Sketch."""
import hashlib

class CountMinSketch:
    def __init__(self, width=100, depth=5):
        self.width = width
        self.depth = depth
        self.table = [[0] * width for _ in range(depth)]

    def _hash(self, item, seed):
        val = f"{seed}:{item}".encode()
        return int(hashlib.md5(val).hexdigest(), 16) % self.width

    def add(self, item, count=1):
        for d in range(self.depth):
            col = self._hash(item, d)
            self.table[d][col] += count

    def estimate(self, item):
        res = float('inf')
        for d in range(self.depth):
            col = self._hash(item, d)
            res = min(res, self.table[d][col])
        return res

if __name__ == "__main__":
    cms = CountMinSketch(width=50, depth=4)
    for _ in range(25):
        cms.add("page_view")
    for _ in range(5):
        cms.add("login")
    assert cms.estimate("page_view") >= 25
    assert cms.estimate("login") >= 5
    print("Day 183 Count-Min Sketch tests passed!")
