"""Day 358: Online Softmax for FlashAttention."""
import math

def online_softmax_update(m_prev, d_prev, x_new):
    m_new = max(m_prev, x_new)
    d_new = d_prev * math.exp(m_prev - m_new) + math.exp(x_new - m_new)
    return m_new, d_new

if __name__ == "__main__":
    stream = [1.0, 3.0, 2.0]
    m, d = -float('inf'), 0.0
    for x in stream:
        m, d = online_softmax_update(m, d, x)
    probs = [math.exp(x - m) / d for x in stream]
    assert abs(sum(probs) - 1.0) < 1e-6
    print("Day 358 FlashAttention Online Softmax tests passed!")
