"""Day 254: Adam Optimizer."""
import math

class AdamOptimizer:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.m = 0.0
        self.v = 0.0
        self.t = 0

    def step(self, param, grad):
        self.t += 1
        self.m = self.beta1 * self.m + (1 - self.beta1) * grad
        self.v = self.beta2 * self.v + (1 - self.beta2) * (grad ** 2)
        m_hat = self.m / (1 - self.beta1 ** self.t)
        v_hat = self.v / (1 - self.beta2 ** self.t)
        return param - self.lr * m_hat / (math.sqrt(v_hat) + self.eps)

if __name__ == "__main__":
    opt = AdamOptimizer(lr=0.1)
    w = 5.0
    w = opt.step(w, grad=2.0)
    assert w < 5.0
    print("Day 254 Adam Optimizer tests passed!")
