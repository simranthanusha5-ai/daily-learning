# Day 46: Big-O Complexity Examples

def constant_time(arr):
    # O(1)
    return arr[0] if arr else None

def linear_time(arr, target):
    # O(n)
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1

def quadratic_time(n):
    # O(n^2)
    pairs = []
    for i in range(n):
        for j in range(n):
            pairs.append((i, j))
    return len(pairs)

print("Constant:", constant_time([10, 20, 30]))
print("Linear search index:", linear_time([1, 3, 5, 7], 5))
print("Quadratic pair count for n=5:", quadratic_time(5))
