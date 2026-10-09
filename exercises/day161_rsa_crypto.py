"""Day 161: RSA Math & Modular Exponentiation."""

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inv(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % phi + phi) % phi

def rsa_encrypt(message_int, e, n):
    return pow(message_int, e, n)

def rsa_decrypt(cipher_int, d, n):
    return pow(cipher_int, d, n)

if __name__ == "__main__":
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = mod_inv(e, phi)
    msg = 65
    c = rsa_encrypt(msg, e, n)
    assert rsa_decrypt(c, d, n) == msg
    print("Day 161 RSA tests passed!")
