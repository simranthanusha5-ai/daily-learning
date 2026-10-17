"""Day 222: Elliptic Curve Math."""

def ec_add(p1, p2, a, p):
    if p1 is None: return p2
    if p2 is None: return p1
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 != y2: return None

    if p1 == p2:
        m = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def ec_multiply(k, point, a, p):
    curr = point
    res = None
    while k > 0:
        if k & 1:
            res = ec_add(res, curr, a, p)
        curr = ec_add(curr, curr, a, p)
        k >>= 1
    return res

if __name__ == "__main__":
    p = 17
    a, b = 2, 2
    G = (5, 1)
    two_G = ec_multiply(2, G, a, p)
    assert two_G is not None
    print("Day 222 Elliptic Curve tests passed!")
