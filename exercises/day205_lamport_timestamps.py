"""Day 205: Lamport Timestamps."""

class LamportNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.clock = 0

    def event(self):
        self.clock += 1
        return (self.clock, self.node_id)

    def send(self):
        self.clock += 1
        return (self.clock, self.node_id)

    def receive(self, remote_ts):
        self.clock = max(self.clock, remote_ts[0]) + 1
        return (self.clock, self.node_id)

if __name__ == "__main__":
    n1 = LamportNode("A")
    n2 = LamportNode("B")
    msg = n1.send()
    ts2 = n2.receive(msg)
    assert ts2[0] == 2
    print("Day 205 Lamport Timestamps tests passed!")
