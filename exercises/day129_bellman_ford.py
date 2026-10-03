"""Day 129: Bellman-Ford Shortest Path Algorithm."""

def bellman_ford(vertices, edges, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Check for negative weight cycles
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist

if __name__ == "__main__":
    nodes = [0, 1, 2, 3]
    edges = [
        (0, 1, 4),
        (0, 2, 5),
        (1, 2, -3),
        (2, 3, 4),
        (1, 3, 2)
    ]
    distances = bellman_ford(nodes, edges, 0)
    assert distances[3] == 6
    print("Day 129 Bellman-Ford tests passed!")
