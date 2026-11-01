"""Day 359: Rotary Position Embeddings (RoPE)."""
import math

def apply_rotary_embedding(x1, x2, pos, theta=10000.0):
    m_theta = pos / theta
    cos_val = math.cos(m_theta)
    sin_val = math.sin(m_theta)
    r1 = x1 * cos_val - x2 * sin_val
    r2 = x1 * sin_val + x2 * cos_val
    return r1, r2

if __name__ == "__main__":
    q1, q2 = 1.0, 0.0
    rq1, rq2 = apply_rotary_embedding(q1, q2, pos=0)
    assert (rq1, rq2) == (1.0, 0.0)
    rq1_pos1, rq2_pos1 = apply_rotary_embedding(q1, q2, pos=1)
    assert rq1_pos1 != q1
    print("Day 359 RoPE tests passed!")
