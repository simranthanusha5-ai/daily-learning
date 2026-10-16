"""Day 211: CRDT PN-Counter."""

class PNCounter:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.p = [0] * num_nodes
        self.n = [0] * num_nodes

    def inc(self, amount=1):
        self.p[self.node_id] += amount

    def dec(self, amount=1):
        self.n[self.node_id] += amount

    def value(self):
        return sum(self.p) - sum(self.n)

    def merge(self, other):
        for i in range(len(self.p)):
            self.p[i] = max(self.p[i], other.p[i])
            self.n[i] = max(self.n[i], other.n[i])

if __name__ == "__main__":
    c1 = PNCounter(0, 2)
    c2 = PNCounter(1, 2)
    c1.inc(10)
    c2.dec(4)
    c1.merge(c2)
    assert c1.value() == 6
    print("Day 211 CRDT PN-Counter tests passed!")
