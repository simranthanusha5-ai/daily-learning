"""Day 177: Skip List implementation."""
import random

class SkipNode:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level=4, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(-float('inf'), max_level)
        self.level = 0

    def _random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, val):
        update = [None] * (self.max_level + 1)
        curr = self.header
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
            update[i] = curr

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.header
            self.level = lvl

        new_node = SkipNode(val, lvl)
        for i in range(lvl + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, val):
        curr = self.header
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == val

if __name__ == "__main__":
    sl = SkipList()
    for num in [3, 6, 7, 9, 12, 19, 17]:
        sl.insert(num)
    assert sl.search(19) is True
    assert sl.search(15) is False
    print("Day 177 Skip List tests passed!")
