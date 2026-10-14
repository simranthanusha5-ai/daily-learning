"""Day 187: Tarjan's Strongly Connected Components."""

def tarjan_scc(adj):
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    on_stack = set()
    sccs = []

    def strongconnect(u):
        nonlocal index
        indices[u] = index
        lowlink[u] = index
        index += 1
        stack.append(u)
        on_stack.add(u)

        for v in adj.get(u, []):
            if v not in indices:
                strongconnect(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif v in on_stack:
                lowlink[u] = min(lowlink[u], indices[v])

        if lowlink[u] == indices[u]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == u:
                    break
            sccs.append(sorted(scc))

    for node in list(adj.keys()):
        if node not in indices:
            strongconnect(node)
    return sccs

if __name__ == "__main__":
    graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [3]
    }
    comps = tarjan_scc(graph)
    assert [3, 4] in comps
    assert [0, 1, 2] in comps
    print("Day 187 Tarjan's SCC tests passed!")
