"""Day 355: Learning With Errors (LWE)."""
import random

Q = 97 # Prime modulus

def lwe_encrypt(bit, s, a, error):
    # b = a*s + e + bit*(q/2)
    b = (a * s + error + bit * (Q // 2)) % Q
    return a, b

def lwe_decrypt(a, b, s):
    val = (b - a * s) % Q
    # If close to Q//2, bit 1; if close to 0, bit 0
    diff = min(val, Q - val)
    return 1 if abs(val - Q // 2) < diff else 0

if __name__ == "__main__":
    secret_s = 5
    a, b = lwe_encrypt(1, secret_s, a=12, error=1)
    dec = lwe_decrypt(a, b, secret_s)
    assert dec == 1
    print("Day 355 LWE tests passed!")
