"""Day 288: Min-Cost Max-Flow (SPFA)."""
from collections import deque

class MCMF:
    def __init__(self, n):
        self.n = n
        self.cap = [[0] * n for _ in range(n)]
        self.cost = [[0] * n for _ in range(n)]

    def add_edge(self, u, v, c, w):
        self.cap[u][v] = c
        self.cost[u][v] = w
        self.cost[v][u] = -w

    def spfa(self, s, t):
        dist = [float('inf')] * self.n
        parent = [-1] * self.n
        in_queue = [False] * self.n
        dist[s] = 0
        q = deque([s])
        in_queue[s] = True

        while q:
            u = q.popleft()
            in_queue[u] = False
            for v in range(self.n):
                if self.cap[u][v] > 0 and dist[u] + self.cost[u][v] < dist[v]:
                    dist[v] = dist[u] + self.cost[u][v]
                    parent[v] = u
                    if not in_queue[v]:
                        q.append(v)
                        in_queue[v] = True
        return parent, dist[t]

    def solve(self, s, t):
        max_flow = 0
        min_cost = 0
        while True:
            parent, d = self.spfa(s, t)
            if parent[t] == -1:
                break
            v = t
            push = float('inf')
            while v != s:
                u = parent[v]
                push = min(push, self.cap[u][v])
                v = u
            v = t
            while v != s:
                u = parent[v]
                self.cap[u][v] -= push
                self.cap[v][u] += push
                min_cost += push * self.cost[u][v]
                v = u
            max_flow += push
        return max_flow, min_cost

if __name__ == "__main__":
    m = MCMF(4)
    m.add_edge(0, 1, 3, 1)
    m.add_edge(0, 2, 2, 2)
    m.add_edge(1, 3, 2, 2)
    m.add_edge(2, 3, 2, 1)
    flow, cost = m.solve(0, 3)
    assert flow == 4
    assert cost == 12
    print("Day 288 Min-Cost Max-Flow tests passed!")
