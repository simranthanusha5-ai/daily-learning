"""Day 356: WebAuthn Authenticator Data."""
import struct
import hashlib

def parse_auth_data(auth_data: bytes):
    rp_id_hash = auth_data[:32]
    flags = auth_data[32]
    sign_count = struct.unpack(">I", auth_data[33:37])[0]
    return {
        "up": bool(flags & 0x01), # User Present
        "uv": bool(flags & 0x04), # User Verified
        "sign_count": sign_count
    }

if __name__ == "__main__":
    sample = hashlib.sha256(b"example.com").digest() + bytes([0x05]) + struct.pack(">I", 10)
    parsed = parse_auth_data(sample)
    assert parsed["up"] is True
    assert parsed["uv"] is True
    assert parsed["sign_count"] == 10
    print("Day 356 WebAuthn tests passed!")
