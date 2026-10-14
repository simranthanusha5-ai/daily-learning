"""Day 190: Dinic's Algorithm."""
from collections import deque

class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.flow = 0
        self.rev = rev

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.level = [-1] * n
        self.ptr = [0] * n

    def add_edge(self, u, v, cap):
        a = Edge(v, cap, None)
        b = Edge(u, 0, None)
        a.rev = b
        b.rev = a
        self.adj[u].append(a)
        self.adj[v].append(b)

    def _bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for edge in self.adj[u]:
                if edge.cap - edge.flow > 0 and self.level[edge.to] == -1:
                    self.level[edge.to] = self.level[u] + 1
                    q.append(edge.to)
        return self.level[t] != -1

    def _dfs(self, u, t, pushed):
        if pushed == 0 or u == t:
            return pushed
        for cid in range(self.ptr[u], len(self.adj[u])):
            self.ptr[u] = cid
            edge = self.adj[u][cid]
            tr = edge.to
            if self.level[u] + 1 != self.level[tr] or edge.cap - edge.flow == 0:
                continue
            push = self._dfs(tr, t, min(pushed, edge.cap - edge.flow))
            if push == 0:
                continue
            edge.flow += push
            edge.rev.flow -= push
            return push
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self._bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                pushed = self._dfs(s, t, float('inf'))
                if pushed == 0:
                    break
                flow += pushed
        return flow

if __name__ == "__main__":
    d = Dinic(4)
    d.add_edge(0, 1, 10)
    d.add_edge(0, 2, 10)
    d.add_edge(1, 2, 2)
    d.add_edge(1, 3, 4)
    d.add_edge(2, 3, 9)
    assert d.max_flow(0, 3) == 13
    print("Day 190 Dinic's Algorithm tests passed!")
