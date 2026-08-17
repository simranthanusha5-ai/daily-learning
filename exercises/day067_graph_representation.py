# Day 67: Graph Representation

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, directed=False):
        self.adj.setdefault(u, []).append(v)
        if not directed:
            self.adj.setdefault(v, []).append(u)

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
print("Graph Adjacency List:", g.adj)
