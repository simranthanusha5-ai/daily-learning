"""Day 348: BLS Signature Aggregation."""

def bls_aggregate(signatures, p=10007):
    # Aggregated signature is vector sum of individual signatures
    agg_x = sum(sig[0] for sig in signatures) % p
    agg_y = sum(sig[1] for sig in signatures) % p
    return (agg_x, agg_y)

if __name__ == "__main__":
    sigs = [(10, 20), (30, 40), (50, 60)]
    agg = bls_aggregate(sigs)
    assert agg == (90, 120)
    print("Day 348 BLS Aggregation tests passed!")
