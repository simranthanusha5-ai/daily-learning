"""Day 185: Interval Tree."""

class IntervalNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max = high
        self.left = None
        self.right = None

class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, low, high):
        self.root = self._insert(self.root, low, high)

    def _insert(self, node, low, high):
        if not node:
            return IntervalNode(low, high)
        if low < node.low:
            node.left = self._insert(node.left, low, high)
        else:
            node.right = self._insert(node.right, low, high)
        node.max = max(node.max, high)
        return node

    def find_overlapping(self, low, high):
        res = []
        def _search(node):
            if not node: return
            if not (node.high < low or node.low > high):
                res.append((node.low, node.high))
            if node.left and node.left.max >= low:
                _search(node.left)
            if node.right:
                _search(node.right)
        _search(self.root)
        return res

if __name__ == "__main__":
    it = IntervalTree()
    it.insert(15, 20)
    it.insert(10, 30)
    it.insert(17, 19)
    it.insert(5, 20)
    it.insert(12, 15)
    it.insert(30, 40)
    overlaps = it.find_overlapping(14, 16)
    assert (15, 20) in overlaps
    assert (10, 30) in overlaps
    print("Day 185 Interval Tree tests passed!")
