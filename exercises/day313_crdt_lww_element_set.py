"""Day 313: CRDT LWW-Element-Set."""

class LWWElementSet:
    def __init__(self):
        self.add_set = {} # elem -> timestamp
        self.remove_set = {} # elem -> timestamp

    def add(self, elem, timestamp):
        self.add_set[elem] = max(self.add_set.get(elem, 0), timestamp)

    def remove(self, elem, timestamp):
        self.remove_set[elem] = max(self.remove_set.get(elem, 0), timestamp)

    def lookup(self, elem):
        if elem in self.add_set:
            if elem not in self.remove_set or self.add_set[elem] > self.remove_set[elem]:
                return True
        return False

    def merge(self, other):
        for e, ts in other.add_set.items():
            self.add_set[e] = max(self.add_set.get(e, 0), ts)
        for e, ts in other.remove_set.items():
            self.remove_set[e] = max(self.remove_set.get(e, 0), ts)

if __name__ == "__main__":
    s1 = LWWElementSet()
    s2 = LWWElementSet()
    s1.add("item1", timestamp=10)
    s2.remove("item1", timestamp=15)
    s1.merge(s2)
    assert s1.lookup("item1") is False
    s1.add("item1", timestamp=20)
    assert s1.lookup("item1") is True
    print("Day 313 LWW-Element-Set tests passed!")
