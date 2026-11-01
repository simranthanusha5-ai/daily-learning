"""Day 364: Symmetric INT8 Quantization."""

def quantize_int8(tensor):
    max_val = max(abs(x) for x in tensor)
    scale = max_val / 127.0 if max_val != 0 else 1.0
    q_tensor = [int(round(x / scale)) for x in tensor]
    return q_tensor, scale

def dequantize_int8(q_tensor, scale):
    return [q * scale for q in q_tensor]

if __name__ == "__main__":
    weights = [0.0, 1.25, -2.5, 5.0]
    q, s = quantize_int8(weights)
    assert q[-1] == 127
    deq = dequantize_int8(q, s)
    assert abs(deq[-1] - 5.0) < 1e-4
    print("Day 364 INT8 Quantization tests passed!")
