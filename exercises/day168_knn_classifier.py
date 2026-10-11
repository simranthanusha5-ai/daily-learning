"""Day 168: K-Nearest Neighbors (KNN) Classifier."""
from collections import Counter

class KNNClassifier:
    def __init__(self, k=3):
        self.k = k
        self.train_X = []
        self.train_y = []

    def fit(self, X, y):
        self.train_X = X
        self.train_y = y

    def predict(self, point):
        dists = [
            (sum((a - b) ** 2 for a, b in zip(point, x)), y)
            for x, y in zip(self.train_X, self.train_y)
        ]
        dists.sort(key=lambda t: t[0])
        nearest = [label for _, label in dists[:self.k]]
        return Counter(nearest).most_common(1)[0][0]

if __name__ == "__main__":
    knn = KNNClassifier(k=3)
    X = [[1, 1], [1, 2], [5, 5], [6, 5]]
    y = [0, 0, 1, 1]
    knn.fit(X, y)
    assert knn.predict([1, 1.5]) == 0
    assert knn.predict([5.5, 5]) == 1
    print("Day 168 KNN tests passed!")
