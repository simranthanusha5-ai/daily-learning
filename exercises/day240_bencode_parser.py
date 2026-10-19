"""Day 240: Bencode Parser."""

def bencode(val):
    if isinstance(val, int):
        return f"i{val}e".encode()
    if isinstance(val, (bytes, bytearray)):
        return f"{len(val)}:".encode() + val
    if isinstance(val, str):
        b = val.encode()
        return f"{len(b)}:".encode() + b
    if isinstance(val, list):
        return b"l" + b"".join(bencode(x) for x in val) + b"e"
    if isinstance(val, dict):
        out = b"d"
        for k in sorted(val.keys()):
            out += bencode(k) + bencode(val[k])
        return out + b"e"

if __name__ == "__main__":
    encoded = bencode({"name": "ubuntu.iso", "size": 1024})
    assert encoded.startswith(b"d")
    assert b"10:ubuntu.iso" in encoded
    print("Day 240 Bencode tests passed!")
