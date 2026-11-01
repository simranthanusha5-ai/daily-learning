"""Day 365: Speculative Decoding."""

def verify_speculative_tokens(draft_tokens, target_probs, draft_probs):
    accepted = []
    for token in draft_tokens:
        p_target = target_probs.get(token, 0.0)
        p_draft = draft_probs.get(token, 1.0)
        if p_target >= p_draft:
            accepted.append(token)
        else:
            break
    return accepted

if __name__ == "__main__":
    draft = ["the", "quick", "brown"]
    target_p = {"the": 0.9, "quick": 0.8, "brown": 0.2}
    draft_p = {"the": 0.8, "quick": 0.7, "brown": 0.5}
    acc = verify_speculative_tokens(draft, target_p, draft_p)
    assert acc == ["the", "quick"]
    print("Day 365 Speculative Decoding tests passed!")
