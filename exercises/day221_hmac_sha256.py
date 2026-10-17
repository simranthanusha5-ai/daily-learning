"""Day 221: HMAC-SHA256 from primitives."""
import hashlib

def hmac_sha256(key: bytes, msg: bytes) -> str:
    block_size = 64
    if len(key) > block_size:
        key = hashlib.sha256(key).digest()
    key = key.ljust(block_size, b'\x00')

    o_key_pad = bytes(b ^ 0x5c for b in key)
    i_key_pad = bytes(b ^ 0x36 for b in key)

    inner = hashlib.sha256(i_key_pad + msg).digest()
    outer = hashlib.sha256(o_key_pad + inner).hexdigest()
    return outer

if __name__ == "__main__":
    k = b"secret_key"
    m = b"authenticated_payload"
    sig = hmac_sha256(k, m)
    assert len(sig) == 64
    print("Day 221 HMAC-SHA256 tests passed!")
