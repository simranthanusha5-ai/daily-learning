"""Day 191: Hopcroft-Karp Maximum Bipartite Matching."""
from collections import deque

def hopcroft_karp(adj_u, n_u, n_v):
    pair_u = [-1] * n_u
    pair_v = [-1] * n_v
    dist = [-1] * n_u

    def bfs():
        queue = deque()
        for u in range(n_u):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        d_nil = float('inf')
        while queue:
            u = queue.popleft()
            if dist[u] < d_nil:
                for v in adj_u[u]:
                    pu = pair_v[v]
                    if pu == -1:
                        d_nil = dist[u] + 1
                    elif dist[pu] == float('inf'):
                        dist[pu] = dist[u] + 1
                        queue.append(pu)
        return d_nil != float('inf')

    def dfs(u):
        for v in adj_u[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = float('inf')
        return False

    matching = 0
    while bfs():
        for u in range(n_u):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching

if __name__ == "__main__":
    adj = {0: [0, 1], 1: [0], 2: [1, 2]}
    res = hopcroft_karp(adj, 3, 3)
    assert res == 3
    print("Day 191 Hopcroft-Karp tests passed!")
