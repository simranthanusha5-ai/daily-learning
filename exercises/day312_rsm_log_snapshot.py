"""Day 312: RSM Log Snapshotting."""

class RSMWithSnapshot:
    def __init__(self):
        self.state = {}
        self.log = []
        self.last_included_index = -1

    def append_log(self, op, k, v):
        self.log.append((op, k, v))

    def apply_all(self):
        for op, k, v in self.log:
            if op == "SET": self.state[k] = v
            elif op == "DEL" and k in self.state: del self.state[k]

    def take_snapshot(self, up_to_index):
        # Compact log up to index
        self.apply_all()
        self.log = self.log[up_to_index + 1:]
        self.last_included_index += (up_to_index + 1)

if __name__ == "__main__":
    rsm = RSMWithSnapshot()
    rsm.append_log("SET", "a", 10)
    rsm.append_log("SET", "b", 20)
    rsm.take_snapshot(1)
    assert len(rsm.log) == 0
    assert rsm.state["a"] == 10
    print("Day 312 RSM Snapshot tests passed!")
