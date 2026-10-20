"""Day 247: Scaled Dot-Product Attention."""
import math

def softmax_vector(v):
    m = max(v)
    exp_v = [math.exp(x - m) for x in v]
    s = sum(exp_v)
    return [x / s for x in exp_v]

def scaled_dot_product_attention(q, k, v, d_k=2):
    # q, k, v are 1D vectors
    dot = sum(qi * ki for qi, ki in zip(q, k))
    score = dot / math.sqrt(d_k)
    # Weight applied to v
    weight = 1.0 # Single key-value pair simplification
    return [weight * vi for vi in v]

if __name__ == "__main__":
    q = [1.0, 0.0]
    k = [1.0, 0.0]
    v = [5.0, 10.0]
    out = scaled_dot_product_attention(q, k, v)
    assert out == [5.0, 10.0]
    print("Day 247 Attention tests passed!")
