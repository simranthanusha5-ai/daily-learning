"""Day 293: Dominator Tree Construction."""

class CFGDominatorTree:
    def __init__(self, n, adj, entry):
        self.n = n
        self.adj = adj
        self.entry = entry

    def compute_immediate_dominators(self):
        # Iterative dominance calculation
        all_nodes = set(range(self.n))
        dom = {i: set(all_nodes) for i in range(self.n)}
        dom[self.entry] = {self.entry}

        changed = True
        while changed:
            changed = False
            for u in range(self.n):
                if u == self.entry:
                    continue
                preds = [p for p in range(self.n) if u in self.adj.get(p, [])]
                if preds:
                    new_dom = set.intersection(*(dom[p] for p in preds)) | {u}
                else:
                    new_dom = {u}
                if new_dom != dom[u]:
                    dom[u] = new_dom
                    changed = True

        idom = {}
        for u in range(self.n):
            strictly_dominating = dom[u] - {u}
            if strictly_dominating:
                # Closest dominator has max set size
                idom[u] = max(strictly_dominating, key=lambda d: len(dom[d]))
        return idom

if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    dt = CFGDominatorTree(4, graph, 0)
    idoms = dt.compute_immediate_dominators()
    assert idoms[3] == 0
    print("Day 293 Dominator Tree tests passed!")
