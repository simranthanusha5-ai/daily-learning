"""Day 147: Merkle Tree."""
import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

class MerkleTree:
    def __init__(self, leaves):
        self.leaves = [hash_data(l) for l in leaves]
        self.root = self._build(self.leaves)

    def _build(self, nodes):
        if not nodes:
            return ""
        if len(nodes) == 1:
            return nodes[0]
        next_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left
            combined = hash_data(left + right)
            next_level.append(combined)
        return self._build(next_level)

if __name__ == "__main__":
    txs = ["tx1", "tx2", "tx3", "tx4"]
    mt = MerkleTree(txs)
    assert len(mt.root) == 64
    print("Day 147 Merkle Tree tests passed!")
