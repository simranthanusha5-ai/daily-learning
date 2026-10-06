"""Day 144: Consistent Hashing Ring."""
import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, replicas=3):
        self.replicas = replicas
        self.ring = []
        self.node_map = {}

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.replicas):
            vnode = f"{node}#{i}"
            h = self._hash(vnode)
            bisect.insort(self.ring, h)
            self.node_map[h] = node

    def remove_node(self, node):
        for i in range(self.replicas):
            vnode = f"{node}#{i}"
            h = self._hash(vnode)
            self.ring.remove(h)
            del self.node_map[h]

    def get_node(self, key):
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0
        return self.node_map[self.ring[idx]]

if __name__ == "__main__":
    ring = ConsistentHashRing()
    ring.add_node("nodeA")
    ring.add_node("nodeB")
    ring.add_node("nodeC")
    target = ring.get_node("user_1024")
    assert target in ["nodeA", "nodeB", "nodeC"]
    print("Day 144 Consistent Hashing tests passed!")
