"""Day 162: SHA-256 Bitwise Primitive Operations."""

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def ch(x, y, z):
    return (x & y) ^ (~x & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def sigma0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def sigma1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

if __name__ == "__main__":
    val = 0x12345678
    assert rotr(val, 4) == 0x81234567
    assert ch(0xFFFFFFFF, 0x12345678, 0x0) == 0x12345678
    print("Day 162 SHA-256 primitives tests passed!")
