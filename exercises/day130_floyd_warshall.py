"""Day 130: Floyd-Warshall All-Pairs Shortest Path."""

def floyd_warshall(n, edges):
    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

if __name__ == "__main__":
    n = 4
    edges = [(0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1)]
    dist = floyd_warshall(n, edges)
    assert dist[0][3] == 9
    print("Day 130 Floyd-Warshall tests passed!")
