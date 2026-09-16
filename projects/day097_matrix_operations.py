# Day 97 Project: Matrix Operations

def matrix_transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

m1 = [[1, 2], [3, 4]]
m2 = [[2, 0], [1, 2]]
print("Transpose of m1:", matrix_transpose(m1))
print("m1 * m2:", matrix_multiply(m1, m2))
