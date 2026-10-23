"""Day 281: Soft Heap with Item Lists."""

class SoftNode:
    def __init__(self, elem):
        self.elements = [elem]
        self.rank = 0
        self.ckey = elem
        self.next = None
        self.child = None

class SoftHeap:
    def __init__(self, eps=0.2):
        self.eps = eps
        self.head = None

    def insert(self, val):
        new_node = SoftNode(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find_min(self):
        curr = self.head
        min_val = float('inf')
        while curr:
            min_val = min(min_val, curr.ckey)
            curr = curr.next
        return min_val

if __name__ == "__main__":
    sh = SoftHeap()
    sh.insert(42)
    sh.insert(12)
    sh.insert(99)
    assert sh.find_min() == 12
    print("Day 281 Soft Heap tests passed!")
