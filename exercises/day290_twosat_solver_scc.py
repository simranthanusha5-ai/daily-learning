"""Day 290: 2-SAT Solver using SCC."""

def solve_2sat(n_vars, clauses):
    # Literal: x -> 2*(x-1), not x -> 2*(x-1) + 1
    def lit(x):
        return 2 * (abs(x) - 1) if x > 0 else 2 * (abs(x) - 1) + 1
    def neg(l):
        return l ^ 1

    adj = [[] for _ in range(2 * n_vars)]
    for u, v in clauses:
        lu, lv = lit(u), lit(v)
        adj[neg(lu)].append(lv)
        adj[neg(lv)].append(lu)

    # Tarjan SCC
    idx = 0
    indices = [-1] * (2 * n_vars)
    lowlink = [0] * (2 * n_vars)
    on_stack = [False] * (2 * n_vars)
    stack = []
    comp = [-1] * (2 * n_vars)
    scc_count = 0

    def dfs(u):
        nonlocal idx, scc_count
        indices[u] = lowlink[u] = idx
        idx += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if indices[v] == -1:
                dfs(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif on_stack[v]:
                lowlink[u] = min(lowlink[u], indices[v])

        if lowlink[u] == indices[u]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                comp[w] = scc_count
                if w == u:
                    break
            scc_count += 1

    for i in range(2 * n_vars):
        if indices[i] == -1:
            dfs(i)

    # Check satisfiability
    for i in range(n_vars):
        if comp[2 * i] == comp[2 * i + 1]:
            return False, None

    assignment = [comp[2 * i] > comp[2 * i + 1] for i in range(n_vars)]
    return True, assignment

if __name__ == "__main__":
    # (x1 or x2) and (-x1 or x2) and (x1 or -x2)
    clauses = [(1, 2), (-1, 2), (1, -2)]
    sat, assign = solve_2sat(2, clauses)
    assert sat is True
    print("Day 290 2-SAT Solver tests passed!")
