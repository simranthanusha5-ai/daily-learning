"""Day 178: Treap (BST + Heap)."""
import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreapNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        elif key > node.key:
            node.right = self._insert(node.right, key)
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        return node

    def search(self, key):
        curr = self.root
        while curr:
            if curr.key == key:
                return True
            curr = curr.left if key < curr.key else curr.right
        return False

if __name__ == "__main__":
    t = Treap()
    for v in [50, 30, 20, 40, 70, 60, 80]:
        t.insert(v)
    assert t.search(40) is True
    assert t.search(99) is False
    print("Day 178 Treap tests passed!")
