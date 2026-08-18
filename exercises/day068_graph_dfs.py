# Day 68: Graph DFS

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    traversal = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))
    return traversal

graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
print("DFS Traversal starting from A:", dfs(graph, "A"))
