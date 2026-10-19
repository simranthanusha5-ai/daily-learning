"""Day 244: Max Pooling Layer."""

def max_pool_2x2(matrix):
    h, w = len(matrix), len(matrix[0])
    out = []
    for i in range(0, h, 2):
        row = []
        for j in range(0, w, 2):
            val = max(matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])
            row.append(val)
        out.append(row)
    return out

if __name__ == "__main__":
    mat = [
        [1, 3, 2, 4],
        [5, 6, 7, 8],
        [9, 1, 3, 5],
        [2, 4, 6, 8]
    ]
    pooled = max_pool_2x2(mat)
    assert pooled == [[6, 8], [9, 8]]
    print("Day 244 Max Pooling tests passed!")
