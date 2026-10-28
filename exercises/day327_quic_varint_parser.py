"""Day 327: QUIC Variable-Length Integer Parser."""

def encode_quic_varint(v: int) -> bytes:
    if v < (1 << 6):
        return bytes([v])
    elif v < (1 << 14):
        return (0x4000 | v).to_bytes(2, 'big')
    elif v < (1 << 30):
        return (0x80000000 | v).to_bytes(4, 'big')
    else:
        return (0xC000000000000000 | v).to_bytes(8, 'big')

def decode_quic_varint(data: bytes, offset: int = 0):
    first = data[offset]
    prefix = first >> 6
    length = 1 << prefix
    raw = data[offset:offset + length]
    val = int.from_bytes(raw, 'big') & ((1 << (8 * length - 2)) - 1)
    return val, offset + length

if __name__ == "__main__":
    for num in [25, 494, 15293, 4948729]:
        enc = encode_quic_varint(num)
        dec, _ = decode_quic_varint(enc)
        assert dec == num
    print("Day 327 QUIC Varint tests passed!")
