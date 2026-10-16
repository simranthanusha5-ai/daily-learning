"""Day 210: CRDT G-Counter."""

class GCounter:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.counts = [0] * num_nodes

    def inc(self, amount=1):
        self.counts[self.node_id] += amount

    def value(self):
        return sum(self.counts)

    def merge(self, other):
        for i in range(len(self.counts)):
            self.counts[i] = max(self.counts[i], other.counts[i])

if __name__ == "__main__":
    g1 = GCounter(0, 3)
    g2 = GCounter(1, 3)
    g1.inc(5)
    g2.inc(3)
    g1.merge(g2)
    assert g1.value() == 8
    print("Day 210 CRDT G-Counter tests passed!")
