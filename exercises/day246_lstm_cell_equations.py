"""Day 246: LSTM Cell Gates."""
import math

def sigmoid(x): return 1.0 / (1.0 + math.exp(-max(min(x, 20), -20)))

class TinyLSTMCell:
    def step(self, x, h_prev, c_prev):
        # Gates
        f = sigmoid(0.5 * x + 0.5 * h_prev) # Forget
        i = sigmoid(0.6 * x + 0.4 * h_prev) # Input
        c_tilde = math.tanh(0.7 * x + 0.3 * h_prev)
        c = f * c_prev + i * c_tilde
        o = sigmoid(0.5 * x + 0.5 * h_prev) # Output
        h = o * math.tanh(c)
        return h, c

if __name__ == "__main__":
    lstm = TinyLSTMCell()
    h, c = lstm.step(1.0, 0.0, 0.0)
    assert h != 0.0
    assert c != 0.0
    print("Day 246 LSTM tests passed!")
