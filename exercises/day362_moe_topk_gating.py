"""Day 362: MoE Top-K Gating Router."""
import math

def softmax(vals):
    m = max(vals)
    exps = [math.exp(v - m) for v in vals]
    s = sum(exps)
    return [e / s for e in exps]

def route_top_k(logits, k=2):
    probs = softmax(logits)
    indexed = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
    top_k = indexed[:k]
    # Renormalize
    total_p = sum(p for _, p in top_k)
    return [(idx, p / total_p) for idx, p in top_k]

if __name__ == "__main__":
    logits = [2.0, 5.0, 1.0, 4.0]
    routing = route_top_k(logits, k=2)
    assert routing[0][0] == 1 # Highest logit 5.0
    assert routing[1][0] == 3 # Second highest 4.0
    print("Day 362 MoE Router tests passed!")
