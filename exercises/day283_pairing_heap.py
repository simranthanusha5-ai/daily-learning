"""Day 283: Pairing Heap."""

class PairNode:
    def __init__(self, key):
        self.key = key
        self.child = None
        self.sibling = None

class PairingHeap:
    def __init__(self):
        self.root = None

    def merge(self, h1, h2):
        if not h1: return h2
        if not h2: return h1
        if h1.key < h2.key:
            h2.sibling = h1.child
            h1.child = h2
            return h1
        else:
            h1.sibling = h2.child
            h2.child = h1
            return h2

    def insert(self, key):
        node = PairNode(key)
        self.root = self.merge(self.root, node)

    def find_min(self):
        return self.root.key if self.root else None

if __name__ == "__main__":
    ph = PairingHeap()
    ph.insert(30)
    ph.insert(10)
    ph.insert(20)
    assert ph.find_min() == 10
    print("Day 283 Pairing Heap tests passed!")
