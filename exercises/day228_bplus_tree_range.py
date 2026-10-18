"""Day 228: B+ Tree Range Scan."""

class LeafNode:
    def __init__(self):
        self.keys = []
        self.values = []
        self.next = None

class SimpleBPlusTree:
    def __init__(self):
        self.first_leaf = LeafNode()

    def range_query(self, start_k, end_k):
        curr = self.first_leaf
        results = []
        while curr:
            for k, v in zip(curr.keys, curr.values):
                if start_k <= k <= end_k:
                    results.append((k, v))
                elif k > end_k:
                    return results
            curr = curr.next
        return results

if __name__ == "__main__":
    tree = SimpleBPlusTree()
    tree.first_leaf.keys = [10, 20, 30]
    tree.first_leaf.values = ["a", "b", "c"]
    n2 = LeafNode()
    n2.keys = [40, 50, 60]
    n2.values = ["d", "e", "f"]
    tree.first_leaf.next = n2
    assert tree.range_query(20, 45) == [(20, "b"), (30, "c"), (40, "d")]
    print("Day 228 B+ Tree tests passed!")
