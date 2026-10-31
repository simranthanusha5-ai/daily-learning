"""Day 354: GHASH Galois Field GF(2^128)."""

def ghash_multiply(x: int, y: int) -> int:
    R = 0xE1000000000000000000000000000000
    z = 0
    v = x
    for i in range(128):
        if (y >> (127 - i)) & 1:
            z ^= v
        if v & 1:
            v = (v >> 1) ^ R
        else:
            v >>= 1
    return z

if __name__ == "__main__":
    res = ghash_multiply(0x1, 0x2)
    assert res != 0
    print("Day 354 GHASH tests passed!")
