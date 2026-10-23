"""Day 282: Fibonacci Heap."""
import math

class FibNode:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.degree = 0
        self.marked = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key, val=None):
        node = FibNode(key, val)
        if not self.min_node:
            self.min_node = node
        else:
            node.right = self.min_node
            node.left = self.min_node.left
            self.min_node.left.right = node
            self.min_node.left = node
            if node.key < self.min_node.key:
                self.min_node = node
        self.total_nodes += 1
        return node

    def get_min(self):
        return self.min_node.key if self.min_node else None

if __name__ == "__main__":
    fib = FibonacciHeap()
    fib.insert(15)
    fib.insert(7)
    fib.insert(23)
    assert fib.get_min() == 7
    print("Day 282 Fibonacci Heap tests passed!")
