"""Day 307: Multi-Paxos with Leader Lease."""

class MultiPaxosLeader:
    def __init__(self, node_id, quorum_size):
        self.node_id = node_id
        self.quorum_size = quorum_size
        self.has_lease = False
        self.log = {}
        self.next_slot = 0

    def establish_lease(self):
        self.has_lease = True

    def propose(self, command):
        assert self.has_lease, "Leader must hold active lease"
        slot = self.next_slot
        self.next_slot += 1
        self.log[slot] = command
        return slot

if __name__ == "__main__":
    ldr = MultiPaxosLeader(1, quorum_size=2)
    ldr.establish_lease()
    s0 = ldr.propose("WRITE x=10")
    s1 = ldr.propose("WRITE y=20")
    assert s0 == 0 and s1 == 1
    assert ldr.log[1] == "WRITE y=20"
    print("Day 307 Multi-Paxos tests passed!")
