"""Day 153: B-Tree Index Node & Search."""

class BTreeNode:
    def __init__(self, t, leaf=True):
        self.t = t  # Minimum degree
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t=3):
        self.root = BTreeNode(t)
        self.t = t

    def search(self, k, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == k:
            return True
        if node.leaf:
            return False
        return self.search(k, node.children[i])

if __name__ == "__main__":
    bt = BTree(t=2)
    bt.root.keys = [10, 20, 30]
    assert bt.search(20) is True
    assert bt.search(25) is False
    print("Day 153 B-Tree tests passed!")
