"""Day 128: Fenwick Tree (Binary Indexed Tree)."""

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, delta):
        i = idx + 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)

    def prefix_sum(self, idx):
        s = 0
        i = idx + 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_sum(self, left, right):
        if left > right:
            return 0
        return self.prefix_sum(right) - (self.prefix_sum(left - 1) if left > 0 else 0)

if __name__ == "__main__":
    bit = FenwickTree(6)
    arr = [2, 1, 4, 6, -1, 5]
    for i, v in enumerate(arr):
        bit.update(i, v)
    assert bit.range_sum(1, 3) == 11
    bit.update(2, 3) # arr[2] += 3 -> 7
    assert bit.range_sum(1, 3) == 14
    print("Day 128 Fenwick Tree tests passed!")
