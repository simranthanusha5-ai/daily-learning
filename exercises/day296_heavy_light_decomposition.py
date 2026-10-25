"""Day 296: Heavy-Light Decomposition."""

class HLD:
    def __init__(self, n, adj, root=0):
        self.n = n
        self.adj = adj
        self.parent = [-1] * n
        self.depth = [0] * n
        self.heavy = [-1] * n
        self.head = list(range(n))
        self.pos = [0] * n
        self.cur_pos = 0

        self._dfs_size(root, -1, 0)
        self._dfs_hld(root, root)

    def _dfs_size(self, u, p, d):
        self.parent[u] = p
        self.depth[u] = d
        size = 1
        max_c_size = 0
        for v in self.adj[u]:
            if v != p:
                c_size = self._dfs_size(v, u, d + 1)
                size += c_size
                if c_size > max_c_size:
                    max_c_size = c_size
                    self.heavy[u] = v
        return size

    def _dfs_hld(self, u, h):
        self.head[u] = h
        self.pos[u] = self.cur_pos
        self.cur_pos += 1
        if self.heavy[u] != -1:
            self._dfs_hld(self.heavy[u], h)
        for v in self.adj[u]:
            if v != self.parent[u] and v != self.heavy[u]:
                self._dfs_hld(v, v)

if __name__ == "__main__":
    tree = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    hld = HLD(4, tree, 0)
    assert hld.head[0] == 0
    assert hld.parent[3] == 1
    print("Day 296 Heavy-Light Decomposition tests passed!")
