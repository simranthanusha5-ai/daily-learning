"""Day 276: Distributed Replicated Key-Value Store Capstone."""

class ReplicatedKVStore:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.log = []
        self.commit_index = -1
        self.state_machine = {}

    def propose_command(self, cmd):
        entry_idx = len(self.log)
        self.log.append(cmd)
        replicated_count = 1
        for peer in self.peers:
            if peer.append_entries(entry_idx, cmd):
                replicated_count += 1
        # Commit if quorum reached
        if replicated_count > (len(self.peers) + 1) // 2:
            self._commit_to(entry_idx)
            return True
        return False

    def append_entries(self, idx, cmd):
        self.log.append(cmd)
        self._commit_to(idx)
        return True

    def _commit_to(self, idx):
        while self.commit_index < idx:
            self.commit_index += 1
            op, k, v = self.log[self.commit_index]
            if op == "SET":
                self.state_machine[k] = v

    def get(self, key):
        return self.state_machine.get(key)

if __name__ == "__main__":
    # Cluster of 3 nodes
    n1 = ReplicatedKVStore(1, [])
    n2 = ReplicatedKVStore(2, [])
    n3 = ReplicatedKVStore(3, [])
    n1.peers = [n2, n3]
    n2.peers = [n1, n3]
    n3.peers = [n1, n2]

    ok = n1.propose_command(("SET", "milestone", "Day 276 Capstone"))
    assert ok is True
    assert n1.get("milestone") == "Day 276 Capstone"
    assert n2.get("milestone") == "Day 276 Capstone"
    assert n3.get("milestone") == "Day 276 Capstone"
    print("Day 276 Distributed Raft KV Capstone tests passed!")
