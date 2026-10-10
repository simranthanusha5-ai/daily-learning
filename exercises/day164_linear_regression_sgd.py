"""Day 164: Linear Regression via Gradient Descent."""

class LinearRegressionGD:
    def __init__(self, lr=0.01, epochs=200):
        self.lr = lr
        self.epochs = epochs
        self.weight = 0.0
        self.bias = 0.0

    def fit(self, X, y):
        n = len(X)
        for _ in range(self.epochs):
            y_pred = [self.weight * x + self.bias for x in X]
            dw = (-2 / n) * sum(x * (y_i - p) for x, y_i, p in zip(X, y, y_pred))
            db = (-2 / n) * sum(y_i - p for y_i, p in zip(y, y_pred))
            self.weight -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, x):
        return self.weight * x + self.bias

if __name__ == "__main__":
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    model = LinearRegressionGD(lr=0.05, epochs=500)
    model.fit(X, y)
    assert abs(model.predict(6) - 12.0) < 0.2
    print("Day 164 Linear Regression tests passed!")
