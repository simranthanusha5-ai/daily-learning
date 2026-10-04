"""Day 134: A* Search Algorithm."""
import heapq

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = [(heuristic(start, goal), 0, start, [start])]
    visited = {}

    while open_set:
        est_total, cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return cost, path

        if current in visited and visited[current] <= cost:
            continue
        visited[current] = cost

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                next_cost = cost + 1
                heapq.heappush(open_set, (next_cost + heuristic((nr, nc), goal), next_cost, (nr, nc), path + [(nr, nc)]))

    return None, []

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    cost, path = a_star(grid, (0, 0), (3, 3))
    assert cost == 6
    print("Day 134 A* Search tests passed!")
