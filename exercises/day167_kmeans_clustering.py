"""Day 167: K-Means Clustering."""

def kmeans(data, k=2, max_iters=50):
    centroids = data[:k]
    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        for pt in data:
            dists = [abs(pt - c) for c in centroids]
            best = dists.index(min(dists))
            clusters[best].append(pt)

        new_centroids = [
            sum(cluster) / len(cluster) if cluster else centroids[i]
            for i, cluster in enumerate(clusters)
        ]
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return centroids

if __name__ == "__main__":
    data = [1, 2, 3, 10, 11, 12]
    c = sorted(kmeans(data, k=2))
    assert abs(c[0] - 2.0) < 0.1
    assert abs(c[1] - 11.0) < 0.1
    print("Day 167 K-Means tests passed!")
