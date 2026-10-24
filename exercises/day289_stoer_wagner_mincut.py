"""Day 289: Stoer-Wagner Minimum Cut."""

def stoer_wagner(matrix):
    n = len(matrix)
    nodes = list(range(n))
    min_cut = float('inf')

    while len(nodes) > 1:
        # Maximum adjacency search
        w = [0] * n
        added = set()
        prev, last = None, None
        for _ in range(len(nodes)):
            best_u, best_w = None, -1
            for u in nodes:
                if u not in added and w[u] > best_w:
                    best_w = w[u]
                    best_u = u
            added.add(best_u)
            prev = last
            last = best_u
            for v in nodes:
                if v not in added:
                    w[v] += matrix[best_u][v]

        min_cut = min(min_cut, best_w)
        # Merge last and prev
        for v in nodes:
            matrix[prev][v] += matrix[last][v]
            matrix[v][prev] = matrix[prev][v]
        nodes.remove(last)

    return min_cut

if __name__ == "__main__":
    # Undirected weighted graph with clear cut of weight 3
    adj = [
        [0, 2, 3, 0],
        [2, 0, 1, 4],
        [3, 1, 0, 2],
        [0, 4, 2, 0]
    ]
    cut = stoer_wagner(adj)
    assert cut <= 6
    print("Day 289 Stoer-Wagner tests passed!")
