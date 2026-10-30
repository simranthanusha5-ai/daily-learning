"""Day 344: Spatial R-Tree."""

class MBR:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def intersects(self, other):
        return not (self.x2 < other.x1 or self.x1 > other.x2 or self.y2 < other.y1 or self.y1 > other.y2)

class RTreeNode:
    def __init__(self, mbr, val=None):
        self.mbr = mbr
        self.val = val
        self.children = []

class MiniRTree:
    def __init__(self):
        self.entries = []

    def insert(self, mbr, val):
        self.entries.append(RTreeNode(mbr, val))

    def query(self, query_mbr):
        return [e.val for e in self.entries if e.mbr.intersects(query_mbr)]

if __name__ == "__main__":
    rtree = MiniRTree()
    rtree.insert(MBR(0, 0, 5, 5), "Park")
    rtree.insert(MBR(10, 10, 20, 20), "Airport")
    res = rtree.query(MBR(4, 4, 8, 8))
    assert res == ["Park"]
    print("Day 344 R-Tree tests passed!")
