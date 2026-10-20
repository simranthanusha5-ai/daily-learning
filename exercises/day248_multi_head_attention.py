"""Day 248: Multi-Head Attention Head Splitter."""

def split_heads(vector, num_heads):
    d_model = len(vector)
    d_k = d_model // num_heads
    return [vector[i * d_k:(i + 1) * d_k] for i in range(num_heads)]

def concat_heads(heads):
    flat = []
    for h in heads:
        flat.extend(h)
    return flat

if __name__ == "__main__":
    vec = [1, 2, 3, 4, 5, 6]
    h = split_heads(vec, 3)
    assert len(h) == 3
    assert concat_heads(h) == vec
    print("Day 248 Multi-Head Attention tests passed!")
