"""Day 279: Van Emde Boas Tree."""
import math

class VEBTree:
    def __init__(self, u):
        self.u = u
        self.min = None
        self.max = None
        if u <= 2:
            self.summary = None
            self.clusters = None
        else:
            self.upper_sqrt = 1 << ((u.bit_length() - 1 + 1) // 2)
            self.lower_sqrt = 1 << ((u.bit_length() - 1) // 2)
            self.summary = VEBTree(self.upper_sqrt)
            self.clusters = [VEBTree(self.lower_sqrt) for _ in range(self.upper_sqrt)]

    def _high(self, x):
        return x // self.lower_sqrt

    def _low(self, x):
        return x % self.lower_sqrt

    def _index(self, h, l):
        return h * self.lower_sqrt + l

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
            return
        if x < self.min:
            x, self.min = self.min, x
        if self.u > 2:
            h = self._high(x)
            l = self._low(x)
            if self.clusters[h].min is None:
                self.summary.insert(h)
            self.clusters[h].insert(l)
        if x > self.max:
            self.max = x

    def contains(self, x):
        if self.min == x or self.max == x:
            return True
        if self.u <= 2 or self.min is None or x < self.min or x > self.max:
            return False
        return self.clusters[self._high(x)].contains(self._low(x))

if __name__ == "__main__":
    veb = VEBTree(16)
    veb.insert(3)
    veb.insert(7)
    veb.insert(14)
    assert veb.contains(3) is True
    assert veb.contains(7) is True
    assert veb.contains(5) is False
    print("Day 279 Van Emde Boas Tree tests passed!")
