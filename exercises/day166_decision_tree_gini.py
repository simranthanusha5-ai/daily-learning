"""Day 166: Decision Tree with Gini Impurity."""

def gini_impurity(y):
    if not y:
        return 0
    total = len(y)
    counts = {}
    for label in y:
        counts[label] = counts.get(label, 0) + 1
    return 1.0 - sum((c / total) ** 2 for c in counts.values())

def best_split(X, y):
    best_gini = float('inf')
    best_thresh = None
    for val in sorted(set(X)):
        left_y = [y[i] for i, x in enumerate(X) if x <= val]
        right_y = [y[i] for i, x in enumerate(X) if x > val]
        if not left_y or not right_y:
            continue
        g = (len(left_y) * gini_impurity(left_y) + len(right_y) * gini_impurity(right_y)) / len(y)
        if g < best_gini:
            best_gini = g
            best_thresh = val
    return best_thresh

if __name__ == "__main__":
    X = [1, 2, 7, 8]
    y = [0, 0, 1, 1]
    thresh = best_split(X, y)
    assert thresh == 2
    print("Day 166 Decision Tree tests passed!")
