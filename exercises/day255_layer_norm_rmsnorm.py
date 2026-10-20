"""Day 255: LayerNorm and RMSNorm."""
import math

def layer_norm(x, eps=1e-5):
    mean = sum(x) / len(x)
    var = sum((val - mean) ** 2 for val in x) / len(x)
    return [(val - mean) / math.sqrt(var + eps) for val in x]

def rms_norm(x, eps=1e-5):
    rms = math.sqrt(sum(val ** 2 for val in x) / len(x) + eps)
    return [val / rms for val in x]

if __name__ == "__main__":
    t = [2.0, 4.0, 6.0]
    ln = layer_norm(t)
    assert abs(sum(ln)) < 1e-6 # Zero mean
    rn = rms_norm(t)
    assert len(rn) == 3
    print("Day 255 Normalization tests passed!")
