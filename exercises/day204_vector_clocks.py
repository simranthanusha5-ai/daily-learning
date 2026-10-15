"""Day 204: Vector Clocks."""

class VectorClock:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.clock = [0] * num_nodes

    def tick(self):
        self.clock[self.node_id] += 1

    def send(self):
        self.tick()
        return list(self.clock)

    def receive(self, remote_clock):
        self.tick()
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], remote_clock[i])

    @staticmethod
    def is_concurrent(c1, c2):
        less = any(a < b for a, b in zip(c1, c2))
        greater = any(a > b for a, b in zip(c1, c2))
        return less and greater

if __name__ == "__main__":
    v1 = VectorClock(0, 2)
    v2 = VectorClock(1, 2)
    msg = v1.send()
    v2.receive(msg)
    assert v2.clock == [1, 2]
    print("Day 204 Vector Clocks tests passed!")
