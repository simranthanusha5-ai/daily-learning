"""Day 249: Sinusoidal Positional Encoding."""
import math

def get_positional_encoding(seq_len, d_model):
    pe = [[0.0] * d_model for _ in range(seq_len)]
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            div = math.pow(10000.0, (2 * i) / d_model)
            pe[pos][i] = math.sin(pos / div)
            if i + 1 < d_model:
                pe[pos][i + 1] = math.cos(pos / div)
    return pe

if __name__ == "__main__":
    enc = get_positional_encoding(4, 8)
    assert enc[0][0] == 0.0 # sin(0) = 0
    assert enc[0][1] == 1.0 # cos(0) = 1
    print("Day 249 Positional Encoding tests passed!")
