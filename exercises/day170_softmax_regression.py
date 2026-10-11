"""Day 170: Softmax and Categorical Cross-Entropy."""
import math

def softmax(logits):
    max_l = max(logits)
    exp_l = [math.exp(x - max_l) for x in logits]
    sum_e = sum(exp_l)
    return [e / sum_e for e in exp_l]

def cross_entropy(probs, target_idx):
    eps = 1e-15
    return -math.log(probs[target_idx] + eps)

if __name__ == "__main__":
    logits = [2.0, 1.0, 0.1]
    probs = softmax(logits)
    assert abs(sum(probs) - 1.0) < 1e-6
    assert probs[0] > probs[1] > probs[2]
    loss = cross_entropy(probs, 0)
    assert loss > 0
    print("Day 170 Softmax tests passed!")
