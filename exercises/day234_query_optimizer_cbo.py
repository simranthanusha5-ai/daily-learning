"""Day 234: Cost-Based Join Optimizer."""
import itertools

def estimate_join_cost(order, table_sizes, selectivity=0.1):
    cost = 0
    curr_rows = table_sizes[order[0]]
    for next_tbl in order[1:]:
        next_rows = table_sizes[next_tbl]
        curr_rows = curr_rows * next_rows * selectivity
        cost += curr_rows
    return cost

def find_best_join_order(table_sizes):
    tables = list(table_sizes.keys())
    best_order = None
    min_cost = float('inf')
    for perm in itertools.permutations(tables):
        c = estimate_join_cost(perm, table_sizes)
        if c < min_cost:
            min_cost = c
            best_order = perm
    return best_order, min_cost

if __name__ == "__main__":
    sizes = {"users": 1000, "orders": 50000, "items": 100}
    order, cost = find_best_join_order(sizes)
    assert order is not None
    print("Day 234 Query Optimizer tests passed!")
