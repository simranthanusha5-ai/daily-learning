"""Day 245: RNN Forward Cell."""
import math

class RNNCell:
    def __init__(self, w_xh=0.5, w_hh=0.2, b=0.0):
        self.w_xh = w_xh
        self.w_hh = w_hh
        self.b = b

    def step(self, x, h_prev):
        raw = x * self.w_xh + h_prev * self.w_hh + self.b
        return math.tanh(raw)

if __name__ == "__main__":
    rnn = RNNCell()
    h0 = 0.0
    h1 = rnn.step(1.0, h0)
    h2 = rnn.step(0.5, h1)
    assert abs(h1 - math.tanh(0.5)) < 1e-6
    print("Day 245 RNN Cell tests passed!")
