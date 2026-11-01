"""Day 360: Grouped-Query Attention (GQA)."""

class KVCache:
    def __init__(self):
        self.k_cache = []
        self.v_cache = []

    def update(self, new_k, new_v):
        self.k_cache.append(new_k)
        self.v_cache.append(new_v)
        return self.k_cache, self.v_cache

def gqa_match_heads(num_q_heads, num_kv_heads):
    ratio = num_q_heads // num_kv_heads
    return {q_idx: q_idx // ratio for q_idx in range(num_q_heads)}

if __name__ == "__main__":
    cache = KVCache()
    k_hist, _ = cache.update([0.1, 0.2], [1.0, 2.0])
    mapping = gqa_match_heads(num_q_heads=8, num_kv_heads=2)
    assert mapping[0] == 0
    assert mapping[7] == 1
    print("Day 360 GQA tests passed!")
