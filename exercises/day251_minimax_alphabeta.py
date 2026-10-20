"""Day 251: Minimax with Alpha-Beta Pruning."""

def alphabeta(depth, node_idx, is_max, values, alpha, beta):
    if depth == 3:
        return values[node_idx]
    if is_max:
        best = -float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_idx * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_idx * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]
    res = alphabeta(0, 0, True, leaf_values, -float('inf'), float('inf'))
    assert res == 5
    print("Day 251 Alpha-Beta Pruning tests passed!")
