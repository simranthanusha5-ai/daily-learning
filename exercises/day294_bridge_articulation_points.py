"""Day 294: Bridges and Articulation Points."""

def find_bridges_and_ap(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = []
    ap = set()

    def dfs(u, p=-1):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        children = 0
        for v in adj[u]:
            if v == p:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.append((u, v))
                if low[v] >= tin[u] and p != -1:
                    ap.add(u)
                children += 1
        if p == -1 and children > 1:
            ap.add(u)

    for i in range(n):
        if tin[i] == -1:
            dfs(i)

    return bridges, list(ap)

if __name__ == "__main__":
    # Two triangles joined by bridge (1, 2)
    edge_list = [(0, 1), (1, 0), (1, 2), (2, 3), (3, 4), (4, 2)]
    br, aps = find_bridges_and_ap(5, edge_list)
    assert (1, 2) in br or (2, 1) in br
    assert 1 in aps or 2 in aps
    print("Day 294 Bridge & AP tests passed!")
