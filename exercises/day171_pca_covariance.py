"""Day 171: PCA Covariance Analysis."""

def center_matrix(data):
    n = len(data)
    d = len(data[0])
    means = [sum(row[j] for row in data) / n for j in range(d)]
    centered = [[row[j] - means[j] for j in range(d)] for row in data]
    return centered, means

def covariance_matrix(centered_data):
    n = len(centered_data)
    d = len(centered_data[0])
    cov = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(d):
            cov[i][j] = sum(row[i] * row[j] for row in centered_data) / (n - 1)
    return cov

if __name__ == "__main__":
    pts = [[1, 2], [2, 3], [3, 4], [4, 5]]
    centered, means = center_matrix(pts)
    cov = covariance_matrix(centered)
    assert abs(cov[0][1] - cov[1][0]) < 1e-6
    print("Day 171 PCA tests passed!")
