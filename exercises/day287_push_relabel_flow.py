"""Day 287: Push-Relabel Maximum Flow."""

def push_relabel_max_flow(capacity, s, t):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    height = [0] * n
    excess = [0] * n
    height[s] = n

    for v in range(n):
        if capacity[s][v] > 0:
            flow[s][v] = capacity[s][v]
            flow[v][s] = -capacity[s][v]
            excess[v] = capacity[s][v]
            excess[s] -= capacity[s][v]

    while True:
        # Find active node
        u = -1
        for i in range(n):
            if i != s and i != t and excess[i] > 0:
                u = i
                break
        if u == -1:
            break

        pushed = False
        for v in range(n):
            if capacity[u][v] - flow[u][v] > 0 and height[u] == height[v] + 1:
                send = min(excess[u], capacity[u][v] - flow[u][v])
                flow[u][v] += send
                flow[v][u] -= send
                excess[u] -= send
                excess[v] += send
                pushed = True
                break
        if not pushed:
            min_h = float('inf')
            for v in range(n):
                if capacity[u][v] - flow[u][v] > 0:
                    min_h = min(min_h, height[v])
            if min_h < float('inf'):
                height[u] = min_h + 1

    return sum(flow[s][i] for i in range(n))

if __name__ == "__main__":
    cap = [
        [0, 10, 10, 0],
        [0, 0, 2, 8],
        [0, 0, 0, 9],
        [0, 0, 0, 0]
    ]
    f = push_relabel_max_flow(cap, 0, 3)
    assert f == 17
    print("Day 287 Push-Relabel tests passed!")
