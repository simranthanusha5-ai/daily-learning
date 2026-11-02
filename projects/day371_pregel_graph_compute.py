"""Day 371: Pregel Graph Compute."""

class Vertex:
    def __init__(self, vid, val, neighbors):
        self.vid = vid
        self.val = val
        self.neighbors = neighbors
        self.inbox = []

def run_pregel_superstep(vertices, compute_fn):
    outbox = {v.vid: [] for v in vertices}
    for v in vertices:
        messages = compute_fn(v, v.inbox)
        for target, msg in messages:
            outbox[target].append(msg)
    for v in vertices:
        v.inbox = outbox[v.vid]

if __name__ == "__main__":
    v1 = Vertex(1, 1.0, [2])
    v2 = Vertex(2, 1.0, [1])
    def pagerank_step(vertex, inbox):
        if inbox:
            vertex.val = sum(inbox)
        share = vertex.val / len(vertex.neighbors)
        return [(nbr, share) for nbr in vertex.neighbors]

    run_pregel_superstep([v1, v2], pagerank_step)
    assert v1.val == 1.0
    print("Day 371 Pregel tests passed!")
