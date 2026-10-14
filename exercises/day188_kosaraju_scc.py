"""Day 188: Kosaraju's SCC."""
from collections import defaultdict

def kosaraju_scc(vertices, edges):
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        rev_adj[v].append(u)

    visited = set()
    order = []

    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)

    for v in vertices:
        if v not in visited:
            dfs1(v)

    visited.clear()
    sccs = []

    def dfs2(u, comp):
        visited.add(u)
        comp.append(u)
        for v in rev_adj[u]:
            if v not in visited:
                dfs2(v, comp)

    for u in reversed(order):
        if u not in visited:
            comp = []
            dfs2(u, comp)
            sccs.append(sorted(comp))
    return sccs

if __name__ == "__main__":
    nodes = [0, 1, 2, 3, 4]
    edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
    res = kosaraju_scc(nodes, edges)
    assert [0, 1, 2] in res
    print("Day 188 Kosaraju's SCC tests passed!")
