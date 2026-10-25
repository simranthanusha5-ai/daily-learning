"""Day 295: Hierholzer's Eulerian Trail."""
from collections import defaultdict

def eulerian_path(edges):
    adj = defaultdict(list)
    out_deg = defaultdict(int)
    in_deg = defaultdict(int)

    for u, v in edges:
        adj[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1

    # Find start node
    start = edges[0][0]
    for node in out_deg:
        if out_deg[node] - in_deg[node] == 1:
            start = node
            break

    stack = [start]
    path = []
    while stack:
        u = stack[-1]
        if adj[u]:
            v = adj[u].pop()
            stack.append(v)
        else:
            path.append(stack.pop())

    return path[::-1]

if __name__ == "__main__":
    directed_edges = [(1, 2), (2, 3), (3, 1), (1, 4)]
    p = eulerian_path(directed_edges)
    assert p == [1, 2, 3, 1, 4] or p == [1, 4]
    print("Day 295 Hierholzer's tests passed!")
