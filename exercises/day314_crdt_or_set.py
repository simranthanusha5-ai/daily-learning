"""Day 314: CRDT OR-Set."""
import uuid

class ORSet:
    def __init__(self):
        self.elements = set() # (element, tag)
        self.tombstones = set() # tags

    def add(self, elem):
        tag = str(uuid.uuid4())
        self.elements.add((elem, tag))
        return tag

    def remove(self, elem):
        for e, tag in list(self.elements):
            if e == elem:
                self.tombstones.add(tag)

    def read(self):
        return {e for e, tag in self.elements if tag not in self.tombstones}

    def merge(self, other):
        self.elements |= other.elements
        self.tombstones |= other.tombstones

if __name__ == "__main__":
    s1 = ORSet()
    s2 = ORSet()
    t1 = s1.add("X")
    s2.merge(s1)
    s1.remove("X")
    s2.add("X") # Concurrent re-add with new tag
    s1.merge(s2)
    assert "X" in s1.read()
    print("Day 314 OR-Set tests passed!")
