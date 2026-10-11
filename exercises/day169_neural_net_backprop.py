"""Day 169: Feedforward Neural Network (Backpropagation)."""
import math

class TinyMLP:
    def __init__(self, lr=0.1):
        self.lr = lr
        self.w1 = 0.5
        self.b1 = 0.0
        self.w2 = 0.5
        self.b2 = 0.0

    def _sigmoid(self, x):
        return 1.0 / (1.0 + math.exp(-max(min(x, 20), -20)))

    def train_step(self, x, target):
        # Forward pass
        h = self._sigmoid(x * self.w1 + self.b1)
        out = self._sigmoid(h * self.w2 + self.b2)

        # Backpropagation
        d_out = (out - target) * (out * (1 - out))
        d_w2 = d_out * h
        d_b2 = d_out

        d_h = (d_out * self.w2) * (h * (1 - h))
        d_w1 = d_h * x
        d_b1 = d_h

        self.w2 -= self.lr * d_w2
        self.b2 -= self.lr * d_b2
        self.w1 -= self.lr * d_w1
        self.b1 -= self.lr * d_b1
        return (out - target) ** 2

if __name__ == "__main__":
    net = TinyMLP(lr=0.5)
    for _ in range(200):
        net.train_step(1.0, 0.0)
    h = net._sigmoid(1.0 * net.w1 + net.b1)
    pred = net._sigmoid(h * net.w2 + net.b2)
    assert pred < 0.2
    print("Day 169 Neural Network tests passed!")
