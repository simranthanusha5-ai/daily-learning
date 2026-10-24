"""Day 292: Johnson's APSP Algorithm."""
import heapq

def dijkstra_weights(adj, s, n):
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def johnsons_apsp(n, edges):
    # Augmented graph with virtual vertex n
    aug_edges = list(edges)
    for v in range(n):
        aug_edges.append((n, v, 0))

    # Bellman-Ford from virtual vertex n
    h = [float('inf')] * (n + 1)
    h[n] = 0
    for _ in range(n):
        for u, v, w in aug_edges:
            if h[u] + w < h[v]:
                h[v] = h[u] + w

    # Reweight edges
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        w_prime = w + h[u] - h[v]
        adj[u].append((v, w_prime))

    # Run Dijkstra from each vertex
    all_dist = []
    for u in range(n):
        d_prime = dijkstra_weights(adj, u, n)
        d_orig = [d_prime[v] + h[v] - h[u] if d_prime[v] < float('inf') else float('inf') for v in range(n)]
        all_dist.append(d_orig)

    return all_dist

if __name__ == "__main__":
    edges = [(0, 1, -1), (1, 2, 3), (0, 2, 4)]
    dist = johnsons_apsp(3, edges)
    assert dist[0][2] == 2
    print("Day 292 Johnson's APSP tests passed!")
