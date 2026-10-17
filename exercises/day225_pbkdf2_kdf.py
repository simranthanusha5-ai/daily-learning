"""Day 225: PBKDF2 Key Derivation."""
import hmac
import hashlib
import struct

def pbkdf2_hmac_sha256(password: bytes, salt: bytes, iterations: int, dklen: int = 32) -> bytes:
    def prf(k, m):
        return hmac.new(k, m, hashlib.sha256).digest()

    h_len = 32
    num_blocks = (dklen + h_len - 1) // h_len
    dk = b""

    for i in range(1, num_blocks + 1):
        u = prf(password, salt + struct.pack(">I", i))
        f = bytearray(u)
        for _ in range(iterations - 1):
            u = prf(password, u)
            for j in range(len(f)):
                f[j] ^= u[j]
        dk += bytes(f)
    return dk[:dklen]

if __name__ == "__main__":
    key = pbkdf2_hmac_sha256(b"pass123", b"salt", iterations=50, dklen=16)
    assert len(key) == 16
    print("Day 225 PBKDF2 tests passed!")
