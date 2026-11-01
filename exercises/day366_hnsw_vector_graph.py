"""Day 366: HNSW Vector Graph Layer."""

def l2_dist(v1, v2):
    return sum((a - b)**2 for a, b in zip(v1, v2))

class HNSWLayer:
    def __init__(self):
        self.nodes = {} # id -> vector
        self.adj = {} # id -> list of neighbors

    def add_node(self, node_id, vector, m=2):
        self.nodes[node_id] = vector
        if not self.adj:
            self.adj[node_id] = []
            return
        # Connect to closest m neighbors
        dists = [(l2_dist(vector, self.nodes[other]), other) for other in self.nodes if other != node_id]
        dists.sort()
        neighbors = [nid for _, nid in dists[:m]]
        self.adj[node_id] = neighbors
        for n in neighbors:
            self.adj[n].append(node_id)

if __name__ == "__main__":
    hnsw = HNSWLayer()
    hnsw.add_node(1, [0.0, 0.0])
    hnsw.add_node(2, [1.0, 1.0])
    hnsw.add_node(3, [0.1, 0.1])
    assert 1 in hnsw.adj[3]
    print("Day 366 HNSW tests passed!")
