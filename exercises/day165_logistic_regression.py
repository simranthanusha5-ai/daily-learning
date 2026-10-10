"""Day 165: Binary Logistic Regression."""
import math

class LogisticRegression:
    def __init__(self, lr=0.1, epochs=300):
        self.lr = lr
        self.epochs = epochs
        self.w = 0.0
        self.b = 0.0

    def _sigmoid(self, z):
        return 1.0 / (1.0 + math.exp(-max(min(z, 20), -20)))

    def fit(self, X, y):
        n = len(X)
        for _ in range(self.epochs):
            for x_i, y_i in zip(X, y):
                pred = self._sigmoid(self.w * x_i + self.b)
                err = pred - y_i
                self.w -= self.lr * err * x_i
                self.b -= self.lr * err

    def predict(self, x):
        return 1 if self._sigmoid(self.w * x + self.b) >= 0.5 else 0

if __name__ == "__main__":
    X = [-2, -1, 1, 2]
    y = [0, 0, 1, 1]
    model = LogisticRegression(lr=0.2, epochs=400)
    model.fit(X, y)
    assert model.predict(3) == 1
    assert model.predict(-3) == 0
    print("Day 165 Logistic Regression tests passed!")
