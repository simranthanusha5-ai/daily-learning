"""Day 316: Distributed Barrier."""

class DistributedBarrier:
    def __init__(self, threshold):
        self.threshold = threshold
        self.arrived = set()
        self.departed = set()
        self.phase = 0

    def enter(self, node_id):
        assert self.phase == 0
        self.arrived.add(node_id)
        if len(self.arrived) == self.threshold:
            self.phase = 1
            return True
        return False

    def leave(self, node_id):
        assert self.phase == 1
        self.departed.add(node_id)
        if len(self.departed) == self.threshold:
            self.arrived.clear()
            self.departed.clear()
            self.phase = 0
            return True
        return False

if __name__ == "__main__":
    b = DistributedBarrier(3)
    b.enter("N1")
    b.enter("N2")
    unlocked = b.enter("N3")
    assert unlocked is True
    assert b.phase == 1
    print("Day 316 Distributed Barrier tests passed!")
