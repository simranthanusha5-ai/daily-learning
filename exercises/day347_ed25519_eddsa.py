"""Day 347: Edwards Curve Point Addition."""

P = 2**255 - 19
D = -121665 * pow(121666, -1, P) % P

def edwards_add(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    x3 = (x1 * y2 + y1 * x2) * pow(1 + D * x1 * x2 * y1 * y2, -1, P) % P
    y3 = (y1 * y2 + x1 * x2) * pow(1 - D * x1 * x2 * y1 * y2, -1, P) % P
    return (x3, y3)

if __name__ == "__main__":
    O = (0, 1) # Neutral identity element
    P1 = (0, 1)
    assert edwards_add(P1, O) == P1
    print("Day 347 Ed25519 Curve tests passed!")
