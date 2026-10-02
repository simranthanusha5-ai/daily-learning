# Day 125: Topological Sort (Kahn's Algorithm)
from collections import deque, defaultdict

def topological_sort(vertices: int, edges: list[tuple[int, int]]) -> list[int]:
    adj = defaultdict(list)
    in_degree = [0] * vertices

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(vertices) if in_degree[i] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != vertices:
        raise ValueError("Graph contains a cycle!")
    return order

# 0 -> 1 -> 3, 0 -> 2 -> 3
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
print("Topological build sequence:", topological_sort(4, edges))
