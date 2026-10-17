"""Day 223: Shamir's Secret Sharing."""
import random

PRIME = 2087

def eval_poly(poly, x, p):
    res = 0
    for coeff in reversed(poly):
        res = (res * x + coeff) % p
    return res

def split_secret(secret, k, n, p=PRIME):
    poly = [secret] + [random.randint(1, p - 1) for _ in range(k - 1)]
    shares = [(x, eval_poly(poly, x, p)) for x in range(1, n + 1)]
    return shares

def recover_secret(shares, p=PRIME):
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        num, den = 1, 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                num = (num * -xm) % p
                den = (den * (xj - xm)) % p
        lagrange = num * pow(den, -1, p) % p
        secret = (secret + yj * lagrange) % p
    return (secret + p) % p

if __name__ == "__main__":
    sec = 1234
    shares = split_secret(sec, k=3, n=5)
    rec = recover_secret(shares[:3])
    assert rec == sec
    print("Day 223 Shamir Secret Sharing tests passed!")
