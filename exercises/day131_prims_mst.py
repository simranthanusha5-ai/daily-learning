"""Day 131: Prim's Minimum Spanning Tree."""
import heapq

def prim_mst(num_nodes, adj):
    visited = set()
    min_heap = [(0, 0, -1)]  # (weight, u, parent)
    mst_edges = []
    total_cost = 0

    while min_heap and len(visited) < num_nodes:
        weight, u, parent = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += weight
        if parent != -1:
            mst_edges.append((parent, u, weight))

        for v, w in adj.get(u, []):
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))

    return total_cost, mst_edges

if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 3)],
        1: [(0, 4), (2, 1), (3, 2)],
        2: [(0, 3), (1, 1), (3, 4)],
        3: [(1, 2), (2, 4)]
    }
    cost, edges = prim_mst(4, graph)
    assert cost == 6
    print("Day 131 Prim's MST tests passed!")
