"""Day 363: Direct Preference Optimization (DPO)."""
import math

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-max(min(x, 20), -20)))

def dpo_loss(pi_win_logp, pi_lose_logp, ref_win_logp, ref_lose_logp, beta=0.1):
    log_ratio_win = pi_win_logp - ref_win_logp
    log_ratio_lose = pi_lose_logp - ref_lose_logp
    diff = beta * (log_ratio_win - log_ratio_lose)
    return -math.log(sigmoid(diff))

if __name__ == "__main__":
    loss = dpo_loss(pi_win_logp=-1.0, pi_lose_logp=-3.0, ref_win_logp=-2.0, ref_lose_logp=-2.0, beta=0.1)
    assert loss > 0
    print("Day 363 DPO Loss tests passed!")
