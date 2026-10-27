"""Day 319: Adaptive Replacement Cache (ARC)."""

class SimpleARC:
    def __init__(self, c=4):
        self.c = c
        self.t1 = [] # Recency
        self.t2 = [] # Frequency
        self.b1 = [] # Ghost recency
        self.b2 = [] # Ghost frequency

    def access(self, page):
        if page in self.t1:
            self.t1.remove(page)
            self.t2.append(page)
            return "HIT_T1"
        if page in self.t2:
            self.t2.remove(page)
            self.t2.append(page)
            return "HIT_T2"
        # Cache miss
        if len(self.t1) + len(self.t2) >= self.c:
            if self.t1:
                evicted = self.t1.pop(0)
                self.b1.append(evicted)
            elif self.t2:
                evicted = self.t2.pop(0)
                self.b2.append(evicted)
        self.t1.append(page)
        return "MISS"

if __name__ == "__main__":
    arc = SimpleARC(2)
    assert arc.access("P1") == "MISS"
    assert arc.access("P1") == "HIT_T1"
    assert arc.access("P2") == "MISS"
    print("Day 319 ARC Cache tests passed!")
